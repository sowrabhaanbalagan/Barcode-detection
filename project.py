import cv2
from pyzbar.pyzbar import decode
import csv

# Load the image containing the barcode
image = cv2.imread('bac.jpeg')  # Replace with the path to your image

# Display the original image
cv2.imshow('Original Image', image)
cv2.waitKey(0)

# Detect and decode the barcode
decoded_objects = decode(image)
if decoded_objects:
    barcode_value = decoded_objects[0].data.decode('utf-8')
    print(f"Detected barcode: {barcode_value}")

    # Get the barcode's bounding box
    rect_points = decoded_objects[0].rect
    x, y, w, h = rect_points

    # Draw a rectangle around the detected barcode
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Display the image with the detected barcode
    cv2.imshow('Image with Barcode', image)
    cv2.waitKey(0)

    # Load the dataset from CSV with the correct encoding
    dataset = {}
    with open('upc_corpus.csv', 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header row if it exists
        for row in csv_reader:
            ean, name = row
            dataset[ean] = name

    # Lookup class label
    class_label = dataset.get(barcode_value, "Unknown")
    print(f"Class Label: {class_label}")
else:
    print("No barcode detected in the image")

cv2.destroyAllWindows()
