import os
import pydicom
from PIL import Image

def convert_dicom_files(source_directory, target_directory, output_format):
    # Create the target directory if it doesn't exist
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    # Get the list of files in the source directory
    files = os.listdir(source_directory)

    # Iterate over the DICOM files in the source directory
    for file in files:
        # Construct the full file path
        file_path = os.path.join(source_directory, file)

        # Check if the path points to a file
        if os.path.isfile(file_path):
            # Load the DICOM file
            try:
                dicom_dataset = pydicom.dcmread(file_path)
            except pydicom.errors.InvalidDicomError:
                print(f"File '{file}' is not a valid DICOM file and cannot be converted.")
                continue

            # Check if the DICOM dataset has the required PixelData element
            if "PixelData" not in dicom_dataset:
                print(f"File '{file}' is missing the required PixelData element and cannot be converted.")
                continue

            # Convert the DICOM pixel data to a numpy array
            pixel_array = dicom_dataset.pixel_array

            # Normalize the pixel values to 8-bit (0-255)
            pixel_array = pixel_array.astype("float")
            pixel_array *= 255.0 / pixel_array.max()
            pixel_array = pixel_array.astype("uint8")

            # Create a PIL image from the pixel array
            image = Image.fromarray(pixel_array)

            # Generate a new file name with the desired output format extension
            new_file_name = os.path.splitext(file)[0] + f".{output_format.lower()}"

            # Construct the target file path
            target_file_path = os.path.join(target_directory, new_file_name)

            # Save the image with the desired output format
            image.save(target_file_path)
            print(f"File '{file}' converted to {output_format.upper()} and saved as '{new_file_name}'.")

    print("Conversion completed.")

# Example usage
source_directory = os.path.join(os.getcwd())
target_directory = os.path.join(os.getcwd(), "output_files")
output_format = input("Enter the desired output format (PNG or JPG): ")

# Validate the user input
if output_format.lower() not in ["png", "jpg"]:
    print("Invalid output format. Please choose either PNG or JPG.")
else:
    convert_dicom_files(source_directory, target_directory, output_format)
