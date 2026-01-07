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

def organize_files(root, target_directory, lang='en', font=None):
    """
    Organizes files in the specified directory.
    """
    target_path = Path(target_directory)
    if not target_path.is_dir():
        CustomMessageDialog(
            root, # Use root as parent
            title=translations[lang]["error_title"],
            message=translations[lang]["error_text"] % target_directory,
            lang=lang,
            font=font
        )
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
        log_message = "\n".join(moved_files_log) # This line was missing
        CustomMessageDialog(
            root, # Use root as parent
            title=translations[lang]["completion_title"],
            message=translations[lang]["completion_log_message"] % log_message,
            lang=lang,
            font=font
        )
    else:
        CustomMessageDialog(
            root, # Use root as parent
            title=translations[lang]["completion_title"],
            message=translations[lang]["completion_no_files_moved"],
            lang=lang,
            font=font
        )

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

class CustomDialog(tk.Toplevel):
    """
    A base class for creating custom, modal dialog boxes.
    """
    def __init__(self, parent, title, message, lang='en', font=None):
        super().__init__(parent)
        self.transient(parent)
        self.parent = parent
        self.lang = lang
        self.font = font
        self.result = None

        self.title(title)
        
        # --- Body for the message ---
        body = ttk.Frame(self)
        self.initial_focus = self.body(body, message)
        body.pack(padx=20, pady=20)

        # --- Frame for the buttons ---
        self.buttonbox()

        # --- Dialog behavior ---
        self.grab_set() # Make modal

        if not self.initial_focus:
            self.initial_focus = self

        self.protocol("WM_DELETE_WINDOW", self.cancel)

        self.center_on_parent()

        self.initial_focus.focus_set()
        self.wait_window(self)

    def center_on_parent(self):
        """Center the dialog over the parent window."""
        self.update_idletasks()
        parent_x = self.parent.winfo_x()
        parent_y = self.parent.winfo_y()
        parent_width = self.parent.winfo_width()
        parent_height = self.parent.winfo_height()
        dialog_width = self.winfo_width()
        dialog_height = self.winfo_height()
        
        x = parent_x + (parent_width - dialog_width) // 2
        y = parent_y + (parent_height - dialog_height) // 2
        self.geometry(f"+{x}+{y}")

    def body(self, master, message):
        """Create the dialog body. Return widget that should have initial focus."""
        # Use a Label with wraplength to control text wrapping
        w = ttk.Label(master, text=message, wraplength=600, justify=tk.LEFT, font=self.font)
        w.pack(padx=5, pady=5)
        return w

    def buttonbox(self):
        """
        Create the button box.
        This method is intended to be overridden in subclasses.
        """
        box = ttk.Frame(self)
        # Example button:
        # w = ttk.Button(box, text="OK", width=10, command=self.ok, default=tk.ACTIVE)
        # w.pack(side=tk.LEFT, padx=5, pady=5)
        box.pack()

    def ok(self, event=None):
        """Standard OK handler."""
        if not self.validate():
            self.initial_focus.focus_set() # put focus back
            return
        self.withdraw()
        self.update_idletasks()
        self.apply()
        self.cancel()

    def cancel(self, event=None):
        """Standard Cancel handler."""
        self.parent.focus_set()
        self.destroy()

    def validate(self):
        """
        Validation hook.
        This method is intended to be overridden in subclasses.
        """
        return 1 # 1 means validation passes

    def apply(self):
        """
        Apply hook.
        This method is intended to be overridden in subclasses.
        """
        pass # override


class CustomConfirmDialog(CustomDialog):
    """
    A custom confirmation dialog with 'Yes' and 'No' buttons.
    """
    def buttonbox(self):
        box = ttk.Frame(self)

        yes_text = translations[self.lang].get('yes_button', 'Yes')
        no_text = translations[self.lang].get('no_button', 'No')

        w = ttk.Button(box, text=yes_text, width=10, command=self.yes_pressed, default=tk.ACTIVE)
        w.pack(side=tk.LEFT, padx=10, pady=(10, 0)) # Padding on top
        w = ttk.Button(box, text=no_text, width=10, command=self.no_pressed)
        w.pack(side=tk.LEFT, padx=10, pady=(10, 0)) # Padding on top

        self.bind("<Return>", self.yes_pressed)
        box.pack(pady=(0, 15)) # Increased bottom padding of the whole box

    def yes_pressed(self, event=None):
        self.result = True
        self.ok()

    def no_pressed(self, event=None):
        self.result = False
        self.cancel()


class CustomMessageDialog(CustomDialog):
    """
    A custom message dialog with a single 'OK' button.
    """
    def buttonbox(self):
        box = ttk.Frame(self)

        ok_text = translations[self.lang].get('ok_button', 'OK')

        w = ttk.Button(box, text=ok_text, width=10, command=self.ok_pressed, default=tk.ACTIVE)
        w.pack(side=tk.LEFT, padx=10, pady=(10, 0)) # Padding on top

        self.bind("<Return>", self.ok_pressed)
        self.bind("<Escape>", self.ok_pressed) # Escape key also closes the dialog

        box.pack(pady=(0, 15)) # Increased bottom padding of the whole box

    def ok_pressed(self, event=None):
        self.result = True # Or just simply close the dialog
        self.ok()


class FileOrganizerApp:
    """
    The main GUI for the File Organizer application.
    """
    def __init__(self, root):
        self.root = root
        self.lang = 'en'
        self.fonts = {} # Declare self.fonts here, but initialize with Font objects later
        self.style = ttk.Style(self.root)
        self.create_widgets()
        self.update_ui_language()

    def create_widgets(self):
        """Create and layout the widgets."""
        # Initialize fonts here after root is fully set up
        self.fonts = {
            "small": font.Font(family="Helvetica", size=10),
            "medium": font.Font(family="Helvetica", size=12),
            "large": font.Font(family="Helvetica", size=14),
        }
        self.root.title(translations[self.lang]['title'])
        try:
            icon_path = get_icon_path()
            if icon_path.exists():
                self.root.iconphoto(True, tk.PhotoImage(file=icon_path))
        except tk.TclError:
            print("Warning: Could not load application icon. Ensure it's a valid PNG/PhotoImage format.")


        # Frame for directory selection
        dir_frame = ttk.Frame(self.root)
        dir_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=(10,5))

        self.root.columnconfigure(0, weight=1) # Make the single column expand

        self.dir_label = ttk.Label(dir_frame, text=translations[self.lang]['directory_label'])
        self.dir_label.grid(row=0, column=0, padx=(0, 5), sticky="w")

        self.dir_path = tk.StringVar()
        self.dir_entry = ttk.Entry(dir_frame, textvariable=self.dir_path, width=50)
        self.dir_entry.grid(row=0, column=1, sticky="ew")
        dir_frame.columnconfigure(1, weight=1) # Make the entry field expand

        self.browse_button = ttk.Button(dir_frame, text=translations[self.lang]['browse_button'], command=self.browse_directory)
        self.browse_button.grid(row=0, column=2, padx=(5, 0))
        
        # Frame for controls
        control_frame = ttk.Frame(self.root)
        control_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=(5,10))

        # Configure control_frame grid to be a 2x2 with equal weight for centering
        control_frame.columnconfigure(0, weight=1)
        control_frame.columnconfigure(1, weight=1)
        control_frame.rowconfigure(0, weight=1)
        control_frame.rowconfigure(1, weight=1)

        # --- Language Setting (Top-Left) ---
        lang_frame = ttk.Frame(control_frame)
        lang_frame.grid(row=0, column=0, pady=5)
        lang_frame.columnconfigure(0, weight=1)
        lang_frame.columnconfigure(1, weight=1)
        
        self.lang_label = ttk.Label(lang_frame, text=translations[self.lang]['language_label'])
        self.lang_label.grid(row=0, column=0, padx=(0,5), sticky="e")

        self.lang_selection = tk.StringVar()
        self.lang_combobox = ttk.Combobox(lang_frame, textvariable=self.lang_selection,
                                          values=list(translations.keys()), state="readonly", width=7)
        self.lang_combobox.grid(row=0, column=1, sticky="w")
        self.lang_combobox.set(self.lang)
        self.lang_combobox.bind("<<ComboboxSelected>>", self.change_language)

        # --- Font Size Setting (Top-Right) ---
        font_frame = ttk.Frame(control_frame)
        font_frame.grid(row=0, column=1, pady=5)
        font_frame.columnconfigure(0, weight=1)
        font_frame.columnconfigure(1, weight=1)

        self.font_size_label = ttk.Label(font_frame, text=translations[self.lang]['font_size_label'])
        self.font_size_label.grid(row=0, column=0, padx=(0,5), sticky="e")

        self.current_font_size_key = tk.StringVar(value="medium")
        self.font_size_combobox = ttk.Combobox(font_frame, textvariable=self.current_font_size_key,
                                               values=["small", "medium", "large"], state="readonly", width=10)
        self.font_size_combobox.grid(row=0, column=1, sticky="w")
        self.font_size_combobox.set(self.current_font_size_key.get())
        self.font_size_combobox.bind("<<ComboboxSelected>>", self.change_font_size)
        
        # --- Instructions Button (Bottom-Left) ---
        self.instructions_button = ttk.Button(control_frame, text=translations[self.lang]['instructions_button'], command=self.show_instructions)
        self.instructions_button.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
        
        # --- Organize Button (Bottom-Right) ---
        self.organize_button = ttk.Button(control_frame, text=translations[self.lang]['organize_button'], command=self.run_organization)
        self.organize_button.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

    def browse_directory(self):
        """Open a dialog to select a directory."""
        directory = filedialog.askdirectory(initialdir=Path.home() / "Downloads")
        if directory:
            self.dir_path.set(directory)

    def show_instructions(self):
        """Show the instruction popup."""
        current_font = self.fonts[self.current_font_size_key.get()]
        CustomMessageDialog(
            self.root,
            title=translations[self.lang]['instructions_title'],
            message=translations[self.lang]['instructions_text'],
            lang=self.lang,
            font=current_font
        )
        
    def run_organization(self):
        """Run the file organization process."""
        target_dir = self.dir_path.get()
        if not target_dir:
            current_font = self.fonts[self.current_font_size_key.get()]
            CustomMessageDialog(
                self.root,
                title=translations[self.lang]['warning_title'],
                message=translations[self.lang]['warning_text'],
                lang=self.lang,
                font=current_font
            )
            return

        current_font = self.fonts[self.current_font_size_key.get()]
        confirm_dialog = CustomConfirmDialog(
            self.root,
            title=translations[self.lang]['confirm_title'],
            message=translations[self.lang]['confirm_text'] % target_dir,
            lang=self.lang,
            font=current_font
        )
        if confirm_dialog.result:
            organize_files(self.root, target_dir, self.lang, current_font)

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

        # For ttk widgets like Label, Entry, and Combobox, .config(font=...) works.
        self.dir_label.config(font=current_font)
        self.dir_entry.config(font=current_font)
        self.lang_label.config(font=current_font)
        self.lang_combobox.config(font=current_font)
        self.font_size_label.config(font=current_font)
        self.font_size_combobox.config(font=current_font)

        # For ttk.Button, we must use a Style.
        self.style.configure('TButton', font=current_font)
        
        # Note: messagebox fonts are system-dependent and cannot be changed.

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
