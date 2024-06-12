import tkinter as tk
from tkinter import messagebox, simpledialog
import threading

class BarcodeScannerApp:
    def __init__(self, root, scanner):
        self.root = root
        self.scanner = scanner
        self.scanner_thread = None
        self.setup_gui()
        self.center_window(200, 300)  # Initial window size: 400x300

    def setup_gui(self):
        self.root.title("Barcode Scanner")
        self.root.geometry("400x300")  # Set the initial size of the window (width x height)

        # Position the start/stop button
        self.start_stop_button = tk.Button(self.root, text="Start Scanner", command=self.toggle_scanner)
        self.start_stop_button.place(relx=0.1, rely=0.2, anchor=tk.W)

        # Position the quit button
        self.quit_button = tk.Button(self.root, text="Quit", command=self.on_closing)
        self.quit_button.place(relx=0.1, rely=0.8, anchor=tk.W)

        # Add a button to set the scan delay
        self.set_delay_button = tk.Button(self.root, text="Set Scan Delay", command=self.prompt_for_delay)
        self.set_delay_button.place(relx=0.1, rely=0.4, anchor=tk.W)

        # Add a label to display the current delay
        self.delay_label = tk.Label(self.root, text=f"Current Delay: {self.scanner.delay} seconds")
        self.delay_label.place(relx=0.1, rely=0.5, anchor=tk.W)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def center_window(self, width, height):
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def toggle_scanner(self):
        if not self.scanner.running:
            self.start_scanner()
        else:
            self.stop_scanner()

    def start_scanner(self):
        if not self.scanner.running:
            self.scanner_thread = threading.Thread(target=self.scanner.run)
            self.scanner_thread.start()
            self.start_stop_button.config(text="Stop Scanner")

    def stop_scanner(self):
        if self.scanner.running:
            self.scanner.running = False
            self.scanner_thread.join()
            self.start_stop_button.config(text="Start Scanner")

    def prompt_for_delay(self):
        delay = simpledialog.askinteger("Input", "Enter scan delay in seconds:", minvalue=1, maxvalue=60)
        if delay is not None:
            self.scanner.delay = delay
            self.update_delay_label()  # Update the delay label after setting the delay

    def update_delay_label(self):
        self.delay_label.config(text=f"Current Delay: {self.scanner.delay} seconds")

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.stop_scanner()
            self.root.destroy()
