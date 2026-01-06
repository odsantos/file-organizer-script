# File Organizer Script
#
# This script organizes files in a specified directory by moving them
# into subdirectories based on their file extension.

import shutil
import sys
from pathlib import Path
import tkinter as tk
from tkinter import font, filedialog, messagebox, ttk

# Import translations
from i18n import translations

def _move_file_with_conflict_resolution(item, dest_dir, lang):
    """
    Moves a single file, handling naming conflicts by appending a number.
    Returns a log message string.
    """
    new_path = dest_dir / item.name
    i = 1
    while new_path.exists():
        new_name = f"{item.stem}_{i}{item.suffix}"
        new_path = dest_dir / new_name
        i += 1

    try:
        shutil.move(str(item), str(new_path))
        return translations[lang]["moved_file_log"] % (item.name, dest_dir.name, new_path.name)
    except Exception as e:
        return translations[lang]["error_moving_file_log"] % (item.name, e)

def organize_files(target_directory, lang='en'):
    """
    Organizes files in the specified directory.
    """
    target_path = Path(target_directory)
    if not target_path.is_dir():
        messagebox.showerror(translations[lang]["error_title"], translations[lang]["error_text"] % target_directory)
        return

    moved_files_log = []
    
    try:
        # Get the path of the script itself to avoid moving it
        script_path = Path(__file__).resolve()
    except NameError:
        # Fallback for when running as a frozen executable (PyInstaller)
        script_path = Path(sys.executable).resolve()

    for item in target_path.iterdir():
        if not item.is_file() or item.resolve() == script_path:
            continue

        file_extension = item.suffix.lower()
        if not file_extension:
            continue

        dir_name = f"{file_extension[1:].upper()} Files"
        dest_dir = target_path / dir_name
        dest_dir.mkdir(exist_ok=True)
        
        log_message = _move_file_with_conflict_resolution(item, dest_dir, lang)
        moved_files_log.append(log_message)
    
    if moved_files_log:
        log_message = "\n".join(moved_files_log)
        messagebox.showinfo(translations[lang]["completion_title"], translations[lang]["completion_log_message"] % log_message)
    else:
        messagebox.showinfo(translations[lang]["completion_title"], translations[lang]["completion_no_files_moved"])

def get_icon_path():
    """
    Get the path to the icon file, works for dev and frozen app.
    """
    if getattr(sys, 'frozen', False):
        # The application is frozen
        base_path = Path(sys._MEIPASS)
    else:
        # The application is running in a normal Python environment
        base_path = Path(__file__).parent
    return base_path / 'assets' / 'images' / 'icon-1024x1024.png'

class FileOrganizerApp:
    """
    The main GUI for the File Organizer application.
    """
    def __init__(self, root):
        self.root = root
        self.lang = 'en'
        self.fonts = {
            "small": font.Font(family="Helvetica", size=10),
            "medium": font.Font(family="Helvetica", size=12),
            "large": font.Font(family="Helvetica", size=14),
        }
        self.create_widgets()
        self.update_ui_language()

    def create_widgets(self):
        """Create and layout the widgets."""
        self.root.title(translations[self.lang]['title'])
        try:
            icon_path = get_icon_path()
            if icon_path.exists():
                self.root.iconphoto(True, tk.PhotoImage(file=icon_path))
        except tk.TclError:
            print("Warning: Could not load application icon. Ensure it's a valid PNG/PhotoImage format.")


        # Frame for directory selection
        dir_frame = ttk.Frame(self.root, padding="10")
        dir_frame.grid(row=0, column=0, columnspan=3, sticky="ew")

        self.dir_label = ttk.Label(dir_frame, text=translations[self.lang]['directory_label'])
        self.dir_label.grid(row=0, column=0, padx=(0, 5), sticky="w")

        self.dir_path = tk.StringVar()
        self.dir_entry = ttk.Entry(dir_frame, textvariable=self.dir_path, width=50)
        self.dir_entry.grid(row=0, column=1, sticky="ew")
        dir_frame.columnconfigure(1, weight=1)

        self.browse_button = ttk.Button(dir_frame, text=translations[self.lang]['browse_button'], command=self.browse_directory)
        self.browse_button.grid(row=0, column=2, padx=(5, 0))
        
        # Frame for controls
        control_frame = ttk.Frame(self.root, padding="10")
        control_frame.grid(row=1, column=0, columnspan=3, sticky="ew")

        # Language selection
        self.lang_label = ttk.Label(control_frame, text=translations[self.lang]['language_label'])
        self.lang_label.pack(side="left", padx=(0, 5))

        self.lang_selection = tk.StringVar()
        self.lang_combobox = ttk.Combobox(control_frame, textvariable=self.lang_selection,
                                          values=list(translations.keys()), state="readonly", width=5)
        self.lang_combobox.pack(side="left", padx=(0, 10))
        self.lang_combobox.set(self.lang) # Set initial value
        self.lang_combobox.bind("<<ComboboxSelected>>", self.change_language)

        # Font Size selection
        self.font_size_label = ttk.Label(control_frame, text=translations[self.lang]['font_size_label'])
        self.font_size_label.pack(side="left", padx=(0, 5))

        self.current_font_size_key = tk.StringVar(value="medium") # Default font size
        self.font_size_combobox = ttk.Combobox(control_frame, textvariable=self.current_font_size_key,
                                               values=["small", "medium", "large"], state="readonly", width=7)
        self.font_size_combobox.pack(side="left", padx=(0, 10))
        self.font_size_combobox.set(self.current_font_size_key.get()) # Set initial value
        self.font_size_combobox.bind("<<ComboboxSelected>>", self.change_font_size)

        # Instructions and Organize buttons
        self.instructions_button = ttk.Button(control_frame, text=translations[self.lang]['instructions_button'], command=self.show_instructions)
        self.instructions_button.pack(side="left")
        
        self.organize_button = ttk.Button(control_frame, text=translations[self.lang]['organize_button'], command=self.run_organization)
        self.organize_button.pack(side="right")

    def browse_directory(self):
        """Open a dialog to select a directory."""
        directory = filedialog.askdirectory(initialdir=Path.home() / "Downloads")
        if directory:
            self.dir_path.set(directory)

    def show_instructions(self):
        """Show the instruction popup."""
        messagebox.showinfo(
            translations[self.lang]['instructions_title'],
            translations[self.lang]['instructions_text']
        )
        
    def run_organization(self):
        """Run the file organization process."""
        target_dir = self.dir_path.get()
        if not target_dir:
            messagebox.showwarning(translations[self.lang]['warning_title'], translations[self.lang]['warning_text'])
            return

        if messagebox.askyesno(
            translations[self.lang]['confirm_title'],
            translations[self.lang]['confirm_text'] % target_dir
        ):
            organize_files(target_dir, self.lang)

    def change_language(self, event=None):
        """Change the application's language based on combobox selection."""
        selected_lang = self.lang_selection.get()
        if selected_lang in translations:
            self.lang = selected_lang
            self.update_ui_language()

    def change_font_size(self, event=None):
        """Change the application's font size based on combobox selection."""
        self.current_font_size_key.set(self.font_size_combobox.get())
        self.apply_fonts_to_widgets()

    def apply_fonts_to_widgets(self):
        """Apply the currently selected font size to all relevant widgets."""
        current_font = self.fonts[self.current_font_size_key.get()]

        self.dir_label.config(font=current_font)
        self.dir_entry.config(font=current_font)
        self.browse_button.config(font=current_font)
        self.instructions_button.config(font=current_font)
        self.organize_button.config(font=current_font)
        self.lang_label.config(font=current_font)
        self.lang_combobox.config(font=current_font)
        self.font_size_label.config(font=current_font)
        self.font_size_combobox.config(font=current_font)
        # Note: messagebox fonts are system-dependent and usually cannot be changed directly via Tkinter

    def update_ui_language(self):
        """Update all UI text elements to the current language."""
        self.root.title(translations[self.lang]['title'])
        self.dir_label.config(text=translations[self.lang]['directory_label'])
        self.browse_button.config(text=translations[self.lang]['browse_button'])
        self.instructions_button.config(text=translations[self.lang]['instructions_button'])
        self.organize_button.config(text=translations[self.lang]['organize_button'])
        self.lang_label.config(text=translations[self.lang]['language_label'])
        self.lang_combobox.set(self.lang)
        self.font_size_label.config(text=translations[self.lang]['font_size_label'])
        # Font size combobox values are fixed keys, but their displayed text might be translated in the future if we use a mapping
        # For now, we update the label and re-apply fonts
        self.apply_fonts_to_widgets()


def main():
    """
    The main function to create and run the GUI.
    """
    root = tk.Tk()
    FileOrganizerApp(root) # Instantiating the app class makes it run
    root.mainloop()

if __name__ == "__main__":
    main()
