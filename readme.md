# DICOM to Image Converter

The **DICOM to Image Converter** is a Python script that allows you to convert DICOM files to image files (PNG or JPG) using the PyDICOM and PIL libraries.

## Prerequisites

- **Python 3.6** or above
- **PyDICOM** library
- **PIL** (Python Imaging Library) library

## Installation

1. Clone the repository or download the script file (`converter.py`) directly.
2. Install the required libraries by running the following command: `pip install pydicom pillow`

## Usage

1. Place your DICOM files in a directory and also converter.py in the same directory 
2. Open the terminal or command prompt and navigate to the directory where the `converter.py` script is located.
3. Run the following command to execute the script: `python converter.py`

4. You will be prompted to enter the following information:
   - **Source Directory:** Enter the path to the directory containing the DICOM files.
   - **Target Directory:** Enter the path to the directory where the converted image files will be saved.
   - **Output Format:** Enter the desired output format (**PNG** or **JPG**).

5. The script will convert each DICOM file in the source directory to the specified output format and save the converted images in the target directory.

6. After the conversion is completed, you will see the status of each file conversion in the console.

7. The converted image files will be saved in the target directory with the same filenames as the original DICOM files, but with the appropriate file extension (`.png` or `.jpg`).

## Notes

- Only valid DICOM files with the required **PixelData** element will be converted. Invalid or unsupported DICOM files will be skipped with a corresponding message.

- The pixel values of the DICOM images are normalized to 8-bit (0-255) before saving as image files.

- The script supports both **PNG** and **JPG** as output formats. Please choose either **"PNG"** or **"JPG"** when prompted.
