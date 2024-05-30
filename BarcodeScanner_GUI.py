import tkinter as tk
from tkinter import messagebox
import threading

class BarcodeScannerApp:
    def __init__(self, root, scanner):
        self.root = root
        self.scanner = scanner
        self.scanner_thread = None
        self.setup_gui()

    def setup_gui(self):
        self.root.title("Barcode Scanner")
        self.start_button = tk.Button(self.root, text="Start Scanner", command=self.start_scanner)
        self.start_button.pack(pady=20)
        self.quit_button = tk.Button(self.root, text="Quit", command=self.on_closing)
        self.quit_button.pack(pady=20)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def start_scanner(self):
        if not self.scanner.running:
            self.scanner_thread = threading.Thread(target=self.scanner.run)
            self.scanner_thread.start()

    def stop_scanner(self):
        if self.scanner.running:
            self.scanner.running = False
            self.scanner_thread.join()

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.stop_scanner()
            self.root.destroy()
