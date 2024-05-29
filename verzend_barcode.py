import socket
import json


def send_barcode(barcode):
    """Deze functie stuurt een barcode naar de database-server"""
    HOST = """127.0.0.1"""
    PORT = 65432

    barcode_str = json.dumps(barcode)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        # Barcode via encode omzetten naar byte-format. Dit is nodig omdat je alleen bytes kunt versturen.
        s.sendall(barcode_str.encode('utf-8'))
        print("Barcode verstuurd!")
        data = s.recv(1024)
        print(data.decode())
        # print(f"Received data")



for i in range(1, 5):
    send_barcode([9789059056749, "+"])
    # send_barcode([9789059056749, "-"])

# send_barcode([9781119149224, "-"])

for i in range(1, 21):
    send_barcode([9781119149224, "-"])    