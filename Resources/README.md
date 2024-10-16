# File Encryption and Decryption Tool

## Overview

This project is a file encryption and decryption tool with a graphical user interface (GUI) built using `Tkinter` and enhanced with drag-and-drop functionality (`TkinterDnD2`). It allows users to securely encrypt and decrypt `.txt` files using the `cryptography` library’s `Fernet` symmetric encryption.

## Key Features

1. **Drag-and-Drop File Selection**: Users can easily drag and drop `.txt` files onto the GUI to select them for encryption or decryption.
2. **Encryption**:
   - Generates a unique encryption key using `Fernet`.
   - Encrypts the content of the selected file, replacing the original text with the encrypted content.
   - Displays the encryption key for the user to save (required for decryption).
3. **Decryption**:
   - Users can input the saved encryption key to decrypt the selected file.
   - Restores the original file content by replacing the encrypted text with the decrypted text.
4. **Reset Functionality**: Clears the file and encryption key fields to reset the interface.
5. **Intuitive GUI**:
   - `Listbox` for file selection and content display.
   - `Text` box for displaying and inputting the encryption key.
   - Buttons for encrypting, decrypting, and resetting the interface.

## Technologies Used

- **Python**: Core programming language.
- **Tkinter**: For building the graphical user interface.
- **TkinterDnD2**: For adding drag-and-drop file functionality.
- **Cryptography (Fernet)**: For secure file encryption and decryption.

## Installation

To run this tool on your local machine, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/encryption-tool.git
    ```
2. Navigate to the project directory:
    ```bash
    cd encryption-tool
    ```
3. Install the required dependencies:
    ```bash
    pip install cryptography tk TkinterDnD2
    ```
4. Run the program:
    ```bash
    python main.py
    ```

## Usage

- **Encrypt a File**: Drag a `.txt` file onto the interface and click the "Encrypt" button. Save the encryption key displayed in the text box.
- **Decrypt a File**: Drag the encrypted `.txt` file, input the saved encryption key, and click the "Decrypt" button.
- **Reset**: Click the "Reset" button to clear the file selection and encryption key fields.

---

