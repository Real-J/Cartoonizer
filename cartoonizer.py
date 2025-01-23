import cv2
import numpy as np

def cartoonize_image(image_path):
    # Read the image
    img = cv2.imread(image_path)
    if img is None:
        print("Image not found!")
        return

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply median blur
    gray_blur = cv2.medianBlur(gray, 7)

    # Detect edges using adaptive thresholding
    edges = cv2.adaptiveThreshold(
        gray_blur, 255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY, 9, 10
    )

    # Apply bilateral filter to smooth colors
    color = cv2.bilateralFilter(img, d=9, sigmaColor=300, sigmaSpace=300)

    # Combine edges and smoothed colors
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    # Display the result
    cv2.imshow("Cartoonized Image", cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
input_image_path = "input_image.jpg"  # Replace with your input image path
cartoonize_image(input_image_path)
