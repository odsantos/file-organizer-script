# File Organizer Script

A simple but powerful Python script to automatically organize the files in a directory into clean, type-based subfolders.

## What It Does

This script scans a target folder (like your `Downloads` directory) and moves files into subfolders based on their file type.

- `document.pdf` -> `PDF Files/`
- `photo.jpg` -> `JPG Files/`
- `archive.zip` -> `ZIP Files/`
- ...and so on!

## Requirements

- Python 3 must be installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## How to Use

1.  Open your terminal or command prompt.

2.  Navigate to the `file_organizer_script` directory.

3.  Run the script using the `python3` command, followed by the path to the directory you want to organize.

    **It's best to wrap the path in quotes (" ")**, especially if it contains spaces.

    **macOS/Linux Example:**
    ```bash
    python3 organizer.py "/home/yourname/Documents"
    ```

    **Windows Example:**
    ```bash
    python3 organizer.py "C:\Users\YourName\Downloads"
    ```

The script will then create the necessary folders and move your files.

## Disclaimer

This script modifies your file system by moving files. It is highly recommended to **back up your important files** before running it for the first time. Use this script at your own risk.