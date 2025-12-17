# File Organizer Script
#
# This script organizes files in a specified directory by moving them
# into subdirectories based on their file extension.

import shutil
import sys
from pathlib import Path
import tkinter as tk
from tkinter import font, filedialog, messagebox, ttk

def organize_files(target_directory):
    """
    Organizes files in the specified directory.
    """
    target_path = Path(target_directory)
    if not target_path.is_dir():
        messagebox.showerror("Error", f"The specified directory does not exist:\n{target_directory}")
        return

    # Create a log of moved files
    moved_files_log = []

    # Get the path of the script/executable to avoid moving it
    try:
        # This works when running from a .py file
        script_path = Path(__file__).resolve()
    except NameError:
        # This works when running from a frozen executable
        script_path = Path(sys.executable).resolve()

    for item in target_path.iterdir():
        # Only process files, ignore directories and the script itself
        if item.is_file() and item.resolve() != script_path:
            file_extension = item.suffix.lower()  # e.g., '.pdf', '.jpg'

            if file_extension:
                # Create a directory name from the extension (e.g., 'PDF Files', 'JPG Files')
                dir_name = f"{file_extension[1:].upper()} Files"
                dest_dir = target_path / dir_name

                # Create the destination directory if it doesn't exist
                dest_dir.mkdir(exist_ok=True)

                # To avoid overwriting, find a new name if the file already exists
                new_path = dest_dir / item.name
                i = 1
                while new_path.exists():
                    new_name = f"{item.stem}_{i}{item.suffix}"
                    new_path = dest_dir / new_name
                    i += 1

                # Move the file
                try:
                    shutil.move(str(item), str(new_path))
                    moved_files_log.append(f"Moved: {item.name} -> {dest_dir.name}/{new_path.name}")
                except Exception as e:
                    moved_files_log.append(f"Error moving {item.name}: {e}")
    
    if moved_files_log:
        log_message = "\n".join(moved_files_log)
        messagebox.showinfo("Organization Complete", f"Organization complete.\n\n{log_message}")
    else:
        messagebox.showinfo("Organization Complete", "No files were moved.")


def get_icon_path():
    """
    Get the path to the icon file.
    Handles running as a script or as a frozen executable.
    """
    if getattr(sys, 'frozen', False):
        # The application is frozen
        base_path = Path(sys._MEIPASS)
    else:
        # The application is running as a normal Python script.
        base_path = Path(__file__).parent
    return base_path / 'assets' / 'images' / 'file-organizer-64-64.gif'


def main():
    """
    The main function to create and run the GUI.
    """
    # --- GUI Setup ---
    root = tk.Tk()
    root.title("File Organizer")
    root.geometry("500x300") # Increased height for the new widget
    root.resizable(False, False)

    # --- Font Management ---
    # Define fonts
    default_font = font.nametofont("TkDefaultFont")
    default_font.configure(family="TkDefaultFont", size=10)

    bold_font = default_font.copy()
    bold_font.configure(weight="bold")

    # --- Icon Setup ---
    try:
        icon_path = get_icon_path()
        if icon_path.exists():
            img = tk.PhotoImage(file=icon_path)
            root.iconphoto(False, img)
    except Exception as e:
        print(f"Error setting icon: {e}")

    # --- Themed Style ---
    style = ttk.Style()
    style.theme_use('clam')
    style.configure("TLabel", font=default_font)
    style.configure("TButton", font=default_font)
    style.configure("TEntry", font=default_font)
    style.configure("TMenubutton", font=default_font)

    # --- Main Frame ---
    main_frame = ttk.Frame(root, padding="20")
    main_frame.pack(fill=tk.BOTH, expand=True)

    # --- Directory Selection ---
    dir_frame = ttk.Frame(main_frame)
    dir_frame.pack(fill=tk.X, pady=10)
    dir_frame.columnconfigure(1, weight=1)

    dir_label = ttk.Label(dir_frame, text="Directory:", font=bold_font)
    dir_label.grid(row=0, column=0, padx=(0, 10), sticky='w')

    selected_dir = tk.StringVar()
    # Set default directory to the user's Downloads folder
    downloads_path = Path.home() / "Downloads"
    if downloads_path.is_dir():
        selected_dir.set(str(downloads_path))

    dir_entry = ttk.Entry(dir_frame, textvariable=selected_dir, state="readonly")
    dir_entry.grid(row=0, column=1, sticky='ew')

    def select_directory():
        # Start browsing from the currently selected directory
        initial_dir = selected_dir.get()
        if not Path(initial_dir).is_dir():
            initial_dir = str(Path.home())

        directory = filedialog.askdirectory(initialdir=initial_dir)
        if directory:
            selected_dir.set(directory)

    browse_button = ttk.Button(dir_frame, text="Browse...", command=select_directory)
    browse_button.grid(row=0, column=2, padx=(10, 0), sticky='e')

    # --- Font Size Selector ---
    font_size_frame = ttk.Frame(main_frame)
    font_size_frame.pack(fill=tk.X, pady=5)

    font_size_label = ttk.Label(font_size_frame, text="Font Size:", font=bold_font)
    font_size_label.pack(side=tk.LEFT, padx=(0, 10))

    font_size = tk.StringVar(value="Medium")
    font_size_combo = ttk.Combobox(font_size_frame, textvariable=font_size, values=["Small", "Medium", "Large"], state="readonly", width=10)
    font_size_combo.pack(side=tk.LEFT)

    def update_font_size(event=None):
        size = font_size.get()
        new_size = 10 # Default to medium
        if size == "Small":
            new_size = 8
        elif size == "Large":
            new_size = 12
        
        default_font.configure(size=new_size)
        bold_font.configure(size=new_size)

    font_size_combo.bind("<<ComboboxSelected>>", update_font_size)

    # --- Action Buttons ---
    button_frame = ttk.Frame(main_frame)
    button_frame.pack(fill=tk.X, pady=20)

    def show_instructions():
        instructions = """1. Click 'Browse...' to select a folder.

   **IMPORTANT: To select a folder, you must first double-click to navigate into it, and then click the 'Open' or 'Select Folder' button.**

2. The selected folder path will appear in the text box.

3. Click 'Organize Files' to start sorting.

4. A confirmation message will appear when complete."""
        messagebox.showinfo("Instructions", instructions)

    instructions_button = ttk.Button(button_frame, text="Instructions", command=show_instructions)
    instructions_button.pack(side=tk.LEFT, padx=10)

    def run_organization():
        directory = selected_dir.get()
        if not directory:
            messagebox.showwarning("Warning", "Please select a directory first.")
            return
        
        confirm = messagebox.askyesno("Confirm", f"Are you sure you want to organize files in:\n{directory}?\n\nThis action cannot be undone.")
        if confirm:
            organize_files(directory)

    organize_button = ttk.Button(button_frame, text="Organize Files", command=run_organization, style="Accent.TButton")
    style.configure("Accent.TButton", font=bold_font) # Make this button bold
    organize_button.pack(side=tk.RIGHT, padx=10)

    root.mainloop()


if __name__ == "__main__":
    main()
