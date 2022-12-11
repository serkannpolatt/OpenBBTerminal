# pylint: disable=c-extension-no-member,protected-access,consider-using-with
# type: ignore
import json
import logging
import pickle
import sys
from typing import List

from PySide6.QtCore import QObject, Qt, Signal
from PySide6.QtNetwork import QHostAddress
from PySide6.QtWebSockets import QWebSocketServer
from PySide6.QtWidgets import QMessageBox

from qt_app.config.qt_settings import QT_PATH, QApplication
from qt_app.core.figure_window import QtPlotlyFigureWindow, active_windows
from qt_app.core.qt_figure import QtFigure

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.INFO)
logger.info("Starting socket server")


class BackendSocketServer(QObject):
    connected = Signal()
    disconnected = Signal()
    data_received = Signal(QtFigure)
    isatty_signal = Signal(bool)
    error = Signal(str)
    to_close = Signal(QMessageBox.StandardButton)

    def __init__(self, parent: QWebSocketServer):
        super().__init__(parent)
        self.server = QWebSocketServer(parent.serverName(), parent.secureMode(), parent)
        self.figures: List[QtFigure] = []
        self.clientConnection = None
        self.websocket_port = pickle.load(open(QT_PATH / "assets/qt_socket", "rb"))

        if self.server.listen(QHostAddress.LocalHost, self.websocket_port):
            logger.info("Listening on port %s", self.websocket_port)
        else:
            logger.error("Error listening on port")
            sys.exit(1)

        # This is needed to prevent the application from closing when the last
        # window is closed.
        #
        # This prevents the application from closing if the following conditions:
        # - The application is started from a users custom script with no running loop (SDK)
        # - The application is started from the command line (OpenBB Terminal) and
        #   the user still has figures open
        #
        # We set the default value to False, so the application will not close
        # when the last window is closed. (OpenBB Terminal)
        self.isatty_signal.connect(
            lambda x: QApplication.instance().setQuitOnLastWindowClosed(x)
        )
        self.isatty_signal.emit(False)

        # Setting up the signal connections
        self.to_close.connect(self.on_to_close)
        self.error.connect(lambda x: logger.error(x))
        self.data_received.connect(lambda x: self.figures.append(x))
        self.server.acceptError.connect(self.onAcceptError)
        self.server.newConnection.connect(self.onNewConnection)

    def onAcceptError(self, accept_error):
        logger.error("Accept Error: %s", accept_error)

    def onNewConnection(self):
        logger.info("New Connection")
        self.clientConnection = self.server.nextPendingConnection()
        self.clientConnection.textMessageReceived.connect(self.processTextMessage)
        self.clientConnection.disconnected.connect(self.socketDisconnected)

    def processTextMessage(self, message):
        """Process the incoming message."""
        logger.info("Message received")
        try:
            # If the message is "init", we create a figure and close it immediately.
            # This is so the first plot doesn't have to wait for the QtWebEngine to initialize.
            if message == "init":
                window = QtPlotlyFigureWindow(QtFigure())
                window.close()
                del window
                return

            if message in ["isatty", "isterminal"]:
                # We've received isatty/isterminal, so we can close
                # the application when the last window is closed.
                if len(active_windows) == 0:
                    logger.info("No windows open, killing app")
                    sys.exit(QApplication.instance().quit())

                self.isatty_signal.emit(True)
                if message == "isterminal":
                    logger.info("Terminal detected, sending popup")
                    # We send a popup to the user asking if they would like
                    # to close all open windows.
                    window = active_windows[0]
                    msg = QMessageBox(
                        QMessageBox.Question,
                        "OpenBB Terminal - Terminal Closed",
                        "OpenBB Terminal has been closed, "
                        "would you like to close all remaining windows?",
                        QMessageBox.Yes | QMessageBox.No,
                        window,
                    )
                    msg.resize(400, 100)
                    msg.buttonClicked.connect(lambda x: self.to_close.emit(x))
                    window.raise_()
                    window.activateWindow()

                    if hasattr(window, "_window"):
                        window._window._download_popup = msg
                    else:
                        setattr(window, "_download_popup", msg)

                    msg.setWindowFlags(msg.windowFlags() | Qt.WindowStaysOnTopHint)
                    msg.show()
                    msg.setWindowFlags(msg.windowFlags() & ~Qt.WindowStaysOnTopHint)
                    msg.show()

                return

            fig = QtFigure(json.loads(message))
            self.data_received.emit(fig)
            fig.show()
            fig._window.closing.connect(lambda: self.figures.remove(fig))

            # This is needed to make sure the window opens on top of the terminal.
            # initially the window is created with the WindowStaysOnTopHint flag set,
            # but this is removed when the window is shown. This is done so the
            # window doesn't stay on top when the user clicks on the window.
            fig._window.setWindowFlags(
                fig._window.windowFlags() | Qt.WindowStaysOnTopHint
            )
            fig._window.show()
            fig._window.setWindowFlags(
                fig._window.windowFlags() & ~Qt.WindowStaysOnTopHint
            )
            fig._window.show()
        except json.JSONDecodeError:
            self.error.emit("Invalid JSON")
            return
        except Exception as e:
            self.error.emit(str(e))
            sys.exit(1)

    def socketDisconnected(self):
        logger.info("Socket Disconnected")
        self.clientConnection.deleteLater()

    def on_to_close(self, message):
        """This is called when the user clicks on the popup asking if they would like
        to close all windows.
        """
        logger.info("Popup clicked with option: %s", message.text())
        if message.text() == "&Yes":
            logger.info("Closing all windows")
            for window in active_windows:
                window.close()
            sys.exit(QApplication.instance().quit())

        logger.info("Some figures open, quitting when the last window is closed")