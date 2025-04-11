import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSlider, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QFont

class SliderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Week 6 - NIM Styling Control")
        self.setGeometry(100, 100, 600, 300)
        self.setStyleSheet("background-color: #1e1e1e; color: white;")

        # Label Nama (tetap, tidak diubah dengan slider)
        self.nameLabel = QLabel("Ni Putu Alvina Putri", self)
        self.nameLabel.setAlignment(Qt.AlignCenter)
        self.nameLabel.setFont(QFont("Arial", 20))
        self.nameLabel.setStyleSheet("color: white; padding: 10px;")

        # Label NIM (akan dikontrol dengan slider)
        self.nimLabel = QLabel("F1D022017", self)
        self.nimLabel.setAlignment(Qt.AlignCenter)
        self.nimLabel.setFont(QFont("Arial", 40))
        self.nimLabel.setStyleSheet("color: rgb(0, 0, 0); background-color: rgb(255, 255, 255); padding: 20px;")

        # Sliders
        self.fontSizeSlider = self.create_slider("Font Size", 20, 60, 40)
        self.bgColorSlider = self.create_slider("Background Color", 0, 255, 255)
        self.fontColorSlider = self.create_slider("Font Color", 0, 255, 0)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.nameLabel)
        layout.addWidget(self.nimLabel)
        layout.addSpacing(20)
        layout.addLayout(self.fontSizeSlider["layout"])
        layout.addLayout(self.bgColorSlider["layout"])
        layout.addLayout(self.fontColorSlider["layout"])

        self.setLayout(layout)
        self.update_label()

    def create_slider(self, label_text, min_val, max_val, default_val):
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(min_val)
        slider.setMaximum(max_val)
        slider.setValue(default_val)
        slider.valueChanged.connect(self.update_label)

        label = QLabel(label_text)
        label.setFont(QFont("Arial", 10))
        label.setStyleSheet("color: white;")

        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(slider)

        return {"slider": slider, "layout": layout}

    def update_label(self):
        font_size = self.fontSizeSlider["slider"].value()
        font_gray = self.fontColorSlider["slider"].value()
        bg_gray = self.bgColorSlider["slider"].value()

        self.nimLabel.setFont(QFont("Arial", font_size))
        self.nimLabel.setStyleSheet(
            f"color: rgb({font_gray}, {font_gray}, {font_gray}); "
            f"background-color: rgb({bg_gray}, {bg_gray}, {bg_gray}); "
            "padding: 20px;"
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SliderApp()
    window.show()
    sys.exit(app.exec_())
