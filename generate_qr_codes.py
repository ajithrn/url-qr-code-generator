import os
import qrcode
import glob
from PIL import Image

def generate_qr_code(url, output_path):
    qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=20, border=2)
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR Code
    img = qr.make_image(fill_color="black", back_color="white")

    # Calculate the size needed to make the width at least 1024 pixels
    current_size = img.size[0]
    if current_size < 1024:
        scale_factor = 1024 / current_size
        new_size = (int(current_size * scale_factor), int(current_size * scale_factor))
        img = img.resize(new_size, Image.NEAREST)

    # Save the image with 300 DPI
    img.save(output_path, dpi=(300, 300))

def process_links(input_file):
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    output_base = os.path.join('output', base_name)

    with open(input_file, 'r') as f:
        links = f.read().splitlines()

    for link in links:
        # Extract the filename and path from the URL
        parts = link.split('/')
        filename = parts[-2] + '.png'  # Use the second-to-last part as the filename
        output_dir = os.path.join(output_base, *parts[3:-2])  # Create the directory structure

        # Create the output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Generate the full output path
        output_path = os.path.join(output_dir, filename)

        # Generate and save the QR code
        generate_qr_code(link, output_path)
        print(f"Generated QR code for {link} at {output_path}")

def main():
    # Ensure 'source' and 'output' directories exist
    os.makedirs('source', exist_ok=True)
    os.makedirs('output', exist_ok=True)

    # Process all .txt files in the 'source' directory
    for input_file in glob.glob('source/*.txt'):
        process_links(input_file)

if __name__ == "__main__":
    main()