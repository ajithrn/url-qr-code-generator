# URL QR Code Generator

This tool generates high-resolution QR codes for links(URL) provided in text files.

## Setup

1. Ensure you have Python 3.x installed on your system.
2. Create a virtual environment:

   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:
   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

4. Install the required packages:

   ```bash
   pip install qrcode[pil]
   ```

## Usage

1. Place your text files containing URLs (one URL per line) in the `source` directory.
2. Run the script:

   ```bash
   python generate_qr_codes.py
   ```

3. QR codes will be generated and saved in the `output` directory, maintaining the structure of the original URLs.

## File Structure

- `generate_qr_codes.py`: The main Python script for generating QR codes.
- `source/`: Input directory containing text files with URLs for which QR codes will be generated.
- `output/`: Output directory where generated QR codes will be saved.

## QR Code Specifications

- Resolution: 300 DPI
- Margin (border): 2 units
- Minimum width: 1024 pixels
- Format: PNG

## Example

For a file named `example-links.txt` in the `source` directory containing a link like:

```plaintext
https://example.com/reports/series/product/department/study-one/
```

The QR code will be saved as:

```plaintext
output/example-links/reports/series/product/department/study-one.png
```

## Notes

- Place all input text files in the `source` directory.
- The script will process all `.txt` files in the `source` directory.
- For each input file, a corresponding folder will be created in the `output` directory.
- The script will create subdirectories as needed within each output folder.
- Each QR code image will be named after the last segment of the URL path.
- QR codes are generated with high resolution and optimal size for easy scanning.