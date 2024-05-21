import barcode
from barcode import Code128
from barcode.writer import ImageWriter

def generate_code128_barcode(data):
    try:
        # Generate Code 128 barcode
        code128 = Code128(data, writer=ImageWriter())
        filename = f'code128_barcode_{data}'
        filepath = code128.save(filename)

        print(f"Code 128 barcode generated: {filepath}")
    except Exception as e:
        print(f"Error generating Code 128 barcode: {e}")

if __name__ == "__main__":
    # Prompt user to enter data for the barcode
    barcode_data = input("Enter data to encode in Code 128 barcode: ").strip()

    # Generate Code 128 barcode based on user input
    if barcode_data:
        generate_code128_barcode(barcode_data)
    else:
        print("Invalid input. Please provide data to encode.")
