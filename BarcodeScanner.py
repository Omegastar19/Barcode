import time
import cv2
import zxingcpp

class BarcodeScanner:
    def __init__(self, database, capture_device=0, delay=1):
        self.database = database
        self.capture_device = capture_device
        self.delay = delay  # Delay in seconds between scans
        self.cap = None
        self.last_scan_time = time.time()

    def initialize_camera(self):
        self.cap = cv2.VideoCapture(self.capture_device)
        if not self.cap.isOpened():
            raise Exception("Error: Could not open camera.")

    def process_barcodes_from_image(self, img):
        results = zxingcpp.read_barcodes(img)
        if results:
            for result in results:
                print(f'Found barcode:'
                      f'\n Text:    "{result.text}"'
                      f'\n Format:   {result.format}'
                      f'\n Content:  {result.content_type}'
                      f'\n Position: {result.position}')
        else:
            print("Could not find any barcode.")

    def scanner_delay(self):
        current_time = time.time()
        if current_time - self.last_scan_time >= self.delay:
            self.last_scan_time = current_time
            return True
        return False

    def run(self):
        self.initialize_camera()
        print("Press 'q' to quit the program.")
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Error: Could not read frame.")
                break
            cv2.imshow('Barcode Scanner', frame)
            if self.scanner_delay():
                self.process_barcodes_from_image(frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    database = {}  # Placeholder for your database
    scanner = BarcodeScanner(database)
    scanner.run()
