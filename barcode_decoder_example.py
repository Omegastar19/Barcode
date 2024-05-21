import cv2
import zxingcpp

# Load the image
img = cv2.imread('code128_barcode_453twgw34g.png')

# Read barcodes from the image
results = zxingcpp.read_barcodes(img)

# Process each barcode result
if results:
    for result in results:
        print('Found barcode:'
              f'\n Text:    "{result.text}"'
              f'\n Format:   {result.format}'
              f'\n Content:  {result.content_type}'
              f'\n Position: {result.position}')
else:
    print("Could not find any barcode.")
