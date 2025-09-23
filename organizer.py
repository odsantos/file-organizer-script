# File Organizer Script
#
# This script organizes files in a specified directory by moving them
# into subdirectories based on their file extension.

import os
import shutil
import sys
from pathlib import Path

def main():
    """
    The main function to organize files.
    """
    # --- INPUT VALIDATION ---
    # Check if a directory path was provided as a command-line argument.
    if len(sys.argv) < 2:
        print("Error: No directory specified.")
        print("Usage: python3 organizer.py \"<path_to_your_folder>\"")
        print(r'Example (Windows): python3 organizer.py "C:\\Users\\YourUser\\Downloads"')
        print('Example (macOS/Linux): python3 organizer.py "/home/youruser/Downloads"')
        return

    target_directory = sys.argv[1]
    target_path = Path(target_directory)

    if not target_path.is_dir():
        print(f"Error: The specified directory does not exist: {target_directory}")
        return
    # --- END INPUT VALIDATION ---

    print(f"Starting to organize files in: {target_directory}")

    for item in target_path.iterdir():
        # Only process files, ignore directories and the script itself
        if item.is_file() and item.name != Path(sys.argv[0]).name:
            file_extension = item.suffix.lower() # e.g., '.pdf', '.jpg'

            if file_extension:
                # Create a directory name from the extension (e.g., 'PDF Files', 'JPG Files')
                dir_name = f"{file_extension[1:].upper()} Files"
                dest_dir = target_path / dir_name

                # Create the destination directory if it doesn't exist
                dest_dir.mkdir(exist_ok=True)

                # Move the file
                try:
                    shutil.move(str(item), str(dest_dir))
                    print(f"Moved: {item.name} -> {dest_dir.name}/")
                except Exception as e:
                    print(f"Error moving {item.name}: {e}")

    print("\nOrganization complete.")

if __name__ == "__main__":
    main()