import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QComboBox, QTextEdit, QPushButton
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class EncryptionApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.encryption_methods = ["Caesar", "Substitution", "Shift", "Vigenere", "SHA256"]

        self.method_label = QLabel("Select Encryption Method:")
        self.method_dropdown = QComboBox()
        self.method_dropdown.addItems(self.encryption_methods)

        self.input_label = QLabel("Enter Text:")
        self.input_text = QTextEdit()

        self.output_label = QLabel("Encrypted Text:")
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)

        self.encrypt_button = QPushButton("Encrypt")
        self.encrypt_button.clicked.connect(self.encrypt_text)

        layout = QVBoxLayout()
        layout.addWidget(self.method_label)
        layout.addWidget(self.method_dropdown)
        layout.addWidget(self.input_label)
        layout.addWidget(self.input_text)
        layout.addWidget(self.output_label)
        layout.addWidget(self.output_text)
        layout.addWidget(self.encrypt_button)

        self.setLayout(layout)
        self.setWindowTitle("Encryption App")
        self.show()

    def encrypt_text(self):
        method = self.method_dropdown.currentText()
        input_text = self.input_text.toPlainText()

        if method == "Caesar":
            encrypted_text = self.caesar_cipher(input_text)
        elif method == "Substitution":
            encrypted_text = self.substitution_cipher(input_text)
        elif method == "Shift":
            encrypted_text = self.shift_cipher(input_text)
        elif method == "Vigenere":
            encrypted_text = self.vigenere_cipher(input_text)
        elif method == "SHA256":
            encrypted_text = self.sha256_hash(input_text)
        else:
            encrypted_text = "Invalid encryption method"

        self.output_text.setPlainText(encrypted_text)

    def caesar_cipher(self, text, shift=3):
        result = ""
        for char in text:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += char
        return result

    def substitution_cipher(self, text):
        # Implement your substitution cipher logic here
        return "Substitution Cipher: Not Implemented"

    def shift_cipher(self, text):
        # Implement your shift cipher logic here
        return "Shift Cipher: Not Implemented"

    def vigenere_cipher(self, text):
        # Implement your Vigenere cipher logic here
        return "Vigenere Cipher: Not Implemented"

    def sha256_hash(self, text):
        password = text.encode('utf-8')
        salt = b'salt'  # You should use a unique salt for each hash
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            iterations=100000,
            salt=salt,
            length=32,
            backend=default_backend()
        )
        key = kdf.derive(password)
        return key.hex()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = EncryptionApp()
    sys.exit(app.exec_())
