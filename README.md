# File Organizer

A simple but powerful utility to automatically organize the files in a directory into clean, type-based subfolders.

## What It Does

This script scans a target folder (like your `Downloads` directory) and moves files into subfolders based on their file type.

- `document.pdf` -> `PDF Files/`
- `photo.jpg` -> `JPG Files/`
- `archive.zip` -> `ZIP Files/`
- ...and so on!

## Features

-   **Easy-to-Use Interface**: A simple and clean graphical user interface (GUI).
-   **Standalone Executables**: No need to install Python or any other dependencies. Just download and run.
-   **Smart Conflict Resolution**: Automatically renames files if a file with the same name already exists in the destination.
-   **Convenient**: Defaults to your "Downloads" folder on first launch.
-   **Accessible**: Features adjustable font sizes (Small, Medium, Large).

## Installation and Usage

### For Most Users (Recommended)

The easiest way to get started is to purchase and download the ready-to-use application from our official Gumroad page.

1.  [Purchase and Download from Gumroad](https://osvaldosantos.gumroad.com/l/file-organizer)
2.  Unzip the downloaded file.
3.  **Windows**: Double-click the `organizer.exe` file.
4.  **macOS**: Double-click the `organizer.app` application. You may need to right-click and select "Open" the first time if you see a security warning.
5.  **Linux**: Make the `organizer` file executable (`chmod +x organizer`) and then run it from your terminal (`./organizer`).

### Using the Application

-   Click the **"Browse..."** button to select the directory you want to organize.
-   Click the **"Organize Files"** button to start the process.
-   A confirmation message will show you a log of what was moved.

### For Developers (Running from Source)

If you want to run the script directly from the source code, you can clone this repository. For version history and source code archives, please see the **[GitHub Releases page](https://github.com/odsantos/file-organizer-script/releases)**.

#### Requirements

-   Python 3 must be installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

#### Running the Script

1.  Clone the repository.
2.  Open your terminal or command prompt.
3.  Navigate to the `file_organizer_script` directory.
4.  Run the script with the following command:
    ```bash
    python3 organizer.py
    ```

## Disclaimer

This script helps you organize your files by moving them. As with any tool that modifies your file system, it's always a good idea to be cautious. We recommend you double-check the selected directory before confirming the action.

## License

This software is a commercial product. Use of this software is subject to the terms and conditions outlined in the **[End-User License Agreement (EULA)](LICENSE.md)**.

## About This Repository

This repository serves as the central hub for the File Organizer project. It contains:
-   The Python source code for the File Organizer desktop application (`organizer.py`).
-   The PHP and HTML files for the official File Organizer website (e.g., `index.php`, `contact.php`, `privacy.php`, `terms.php`).

## Support and Contact

If you have any questions, encounter issues, or require support, please visit our official website and use the contact form:
**[File Organizer Contact Page](https://fileorganizer.odsantos.com/contact.php)**