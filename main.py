import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView

class YouTubeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YouTube PyQt Player")
        self.resize(900, 600)

        # Central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Input bar for YouTube link
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Paste YouTube URL or embed link here...")
        layout.addWidget(self.url_input)

        self.btn_load = QPushButton("Load Video")
        self.btn_load.clicked.connect(self.load_video)
        layout.addWidget(self.btn_load)

        # Web view to display YouTube
        self.browser = QWebEngineView()
        layout.addWidget(self.browser)

        # Load a default embed video
        self.browser.setUrl(QUrl("https://youtube.com"))

    def load_video(self):
        url_text = self.url_input.text().strip()
        # Convert standard watch URL to embed URL if necessary
        if "watch?v=" in url_text:
            url_text = url_text.replace("watch?v=", "embed/")
        elif "youtu.be/" in url_text:
            video_id = url_text.split("youtu.be/")[-1]
            url_text = f"https://youtube.com{video_id}"
        
        self.browser.setUrl(QUrl(url_text))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = YouTubeWindow()
    window.show()
    sys.exit(app.exec_())
