# File Organizer

A simple utility to automatically organize the files in a directory into clean, type-based subfolders.

## What It Does

This script scans a target folder (like your `Downloads` directory) and moves files into subfolders based on their file type.

- `document.pdf` -> `PDF Files/`
- `photo.jpg` -> `JPG Files/`
- `archive.zip` -> `ZIP Files/`
- ...and so on!

## Features

- **Easy-to-Use Interface**: A simple and clean graphical user interface (GUI).
- **Standalone Executables**: No need to install Python. Just download and run.
- **Direct Access**: When unzipped, you will find the app files directly (no `dist` folder nesting).
- **Smart Conflict Resolution**: Automatically renames files (e.g., `file_1.jpg`) if a duplicate exists in the destination.
- **Self-Aware**: The application will never move its own executable or script, even if it's sitting inside the folder being organized.
- **Accessible**: Features adjustable font sizes (Small, Medium, Large).
- **Multi-language Support**: Fully translated into English and Portuguese.

## Installation and Usage

### For Most Users (Recommended)

The easiest way to get started is to download the ready-to-use application from our official page.

1. [Download from Gumroad](https://osvaldosantos.gumroad.com/l/file-organizer)
2. **Windows**: Unzip the file. You will see `File Organizer.exe`. Double-click to run it.
3. **macOS**: Unzip the file. You will see a `File Organizer.app` folder. Drag it to your Applications folder or open it directly.
   *Note: You may need to **Right-Click > Open** the first time to bypass security warnings.*
4. **Linux**: Download the `File-Organizer-Linux.AppImage`. 
   *Note: You must make it executable first (`chmod +x File-Organizer-Linux.AppImage`) and then run it.*

### Using the Application

- Click the **"Browse..."** button to select the directory you want to organize.
- Click the **"Organize Files"** button to start the process.
- A confirmation message will show you a log of what was moved.

### For Developers (Running from Source)

To run the script directly from the source code:

#### Requirements
- Python 3.x installed.
- The `Pillow` library (for icon handling).
- The `assets/` folder and `i18n.py` must be in the same directory as `organizer.py`.

#### Running the Script
1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install pillow
   ```
3. Run the application:
    ```bash
    python3 organizer.py
    ```

## Disclaimer

This script helps you organize your files by moving them. As with any tool that modifies your file system, it's always a good idea to be cautious. We recommend you double-check the selected directory before confirming the action.

## License

This project is open-source software licensed under the [MIT License](LICENSE).

### AI Collaboration

This utility was built in collaboration with **Gemini (Google AI)**. It represents a "Human-in-the-Loop" development model where AI logic is refined and verified by the developer.

## About This Repository

This repository serves as the central hub for the File Organizer project. It contains:

- The Python source code (`organizer.py`) and translation logic (`i18n.py`).
- The PHP/HTML files for the official website.
- Automated GitHub Actions workflow (build.yml) for cross-platform releases.

## Support and Contact

If you have any questions, encounter issues, or require support, please visit our official website and use the contact form:

- English: [fileorganizer.odsantos.com/contact.php](https://fileorganizer.odsantos.com/contact.php)
- Português: [fileorganizer.odsantos.com/ao/contact.php](https://fileorganizer.odsantos.com/ao/contact.php)
