# Cartoonizer

A Python script to transform real images into cartoon-like images using OpenCV. The script utilizes edge detection and bilateral filtering techniques to create a visually appealing cartoon effect.

## Features
- Converts real images to cartoon-style images.
- Uses adaptive thresholding for edge detection.
- Applies bilateral filtering for color smoothing.

## Requirements
- Python 3.x
- OpenCV
- NumPy

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Real-J/cartoonizer.git
   cd cartoonizer
   ```

2. Install the required Python packages:
   ```bash
   pip install opencv-python numpy
   ```

## Usage

1. Place your input image in the same directory as the script or specify the full path to the image.

2. Run the script:
   ```bash
   python cartoonizer.py
   ```

3. Replace the `input_image.jpg` in the script with the path to your image file:
   ```python
   input_image_path = "path_to_your_image.jpg"
   ```

4. The cartoonized image will be displayed in a pop-up window.

## Example
### Input Image:
![Input Image](c1.jpg)

### Cartoonized Image:
![Cartoonized Image](c2.jpg)



## Contributing
Feel free to fork this repository and make your changes. Pull requests are welcome!

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

