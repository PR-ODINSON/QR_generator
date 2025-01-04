# Enhanced QR Code Generator

## Project Description
This project is a Python-based application to generate visually appealing QR codes, similar to the QR codes seen on platforms like Instagram or LinkedIn. It provides a graphical user interface (GUI) using `tkinter` and allows users to customize the QR codes with rounded modules, gradient colors, and embedded logos.

---

## Features
- **User-Friendly GUI**: Simple and interactive interface built with `tkinter`.
- **Styled QR Codes**:
  - Rounded modules for a modern look.
  - Customizable radial gradient colors.
- **Logo Embedding**: Option to include a logo at the center of the QR code.
- **Automatic Save**: Saves the generated QR code as an image file (`enhanced_qrcode.png`).

---

## Technologies Used
- **Python**
- **Libraries**:
  - `qrcode`
  - `tkinter`
  - `Pillow` (for handling images)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/enhanced-qr-code-generator.git
   cd enhanced-qr-code-generator
   ```

2. Install the required libraries:
   ```bash
   pip install qrcode[pil] pillow
   ```

3. Add a custom logo (optional):
   - Place your logo file in the project directory and name it `logo.png`.

---

## How to Use

1. Run the application:
   ```bash
   python qr_code_generator.py
   ```

2. Enter the data you want encoded in the QR code into the text field.

3. Click the **Generate QR Code** button.

4. The generated QR code will be displayed within the application and saved as `enhanced_qrcode.png`.

---

## Example Output
- **With Logo**: A QR code featuring a centered logo with rounded modules and gradient colors.
- **Without Logo**: A sleek QR code with customized styling but no logo.

---

## Project Structure
```
.
├── qr_code_generator.py  # Main application script
├── logo.png              # Optional logo file (user-provided)
└── enhanced_qrcode.png   # Generated QR code output
```

---

## Customization
You can customize the following:
- **Colors**:
  - Modify the gradient colors in the `RadialGradiantColorMask` section.
  - Example: `center_color=(0, 102, 255)` (blue center), `edge_color=(0, 51, 102)` (dark blue edge).
- **Logo**:
  - Replace `logo.png` with your preferred logo file (recommended size: 80x80 pixels).
- **Rounded Modules**:
  - The `RoundedModuleDrawer` can be replaced with other module styles from the `qrcode.image.styles.moduledrawers` module.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Contributing
Contributions are welcome! Feel free to fork this repository and submit a pull request.

---

## Author
[Your Name](https://github.com/yourusername)

---

## Acknowledgments
Special thanks to the creators of the `qrcode` and `Pillow` libraries for making this project possible.

