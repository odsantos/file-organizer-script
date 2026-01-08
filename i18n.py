# i18n.py
"""
Internationalization (i18n) translations for the File Organizer application.

This module contains a dictionary of translations for various UI elements
and messages used in the application.
"""

translations = {
    "en": {
        "title": "File Organizer",
        "directory_label": "Directory:",
        "browse_button": "Browse...",
        "font_size_label": "Font Size:",
        "font_size_small": "Small",
        "font_size_medium": "Medium",
        "font_size_large": "Large",
        "instructions_button": "Instructions",
        "organize_button": "Organize Files",
        "language_label": "Language:",
        "instructions_title": "Instructions",
        "instructions_text": """1. Click 'Browse...' to select a folder.

   **IMPORTANT: To select a folder, you must first double-click to navigate
   into it, and then click the 'Open' or 'Select Folder' button.**

2. The selected folder path will appear in the text box.

3. Click 'Organize Files' to start sorting.

4. A confirmation message will appear when complete.""",
        "warning_title": "Warning",
        "warning_text": "Please select a directory first.",
        "confirm_title": "Confirm",
        "confirm_text": "Are you sure you want to organize files in:\n%s?\n\nThis action cannot be undone.",
        "error_title": "Error",
        "error_text": "The specified directory does not exist:\n%s",
        "completion_title": "Organization Complete",
        "completion_log_message": "Organization complete.\n\n%s",
        "completion_no_files_moved": "No files were moved.",
        "moved_file_log": "Moved: %s -> %s/%s",
        "error_moving_file_log": "Error moving %s: %s",
        "yes_button": "Yes",
        "no_button": "No",
        "ok_button": "OK",
        "folder_name_template": "%s Files",
    },
    "pt": {
        "title": "Organizador de Ficheiros",
        "directory_label": "Diretório:",
        "browse_button": "Procurar...",
        "font_size_label": "Tamanho da Fonte:",
        "font_size_small": "Pequeno",
        "font_size_medium": "Médio",
        "font_size_large": "Grande",
        "instructions_button": "Instruções",
        "organize_button": "Organizar Ficheiros",
        "language_label": "Idioma:",
        "instructions_title": "Instruções",
        "instructions_text": """1. Clique em 'Procurar...' para selecionar uma pasta.

   **IMPORTANTE: Para selecionar uma pasta, deve primeiro fazer duplo clique para entrar nela e, e seguida, clicar no botão 'Abrir' ou 'Selecionar Pasta'.**

2. O caminho da pasta selecionada aparecerá na caixa de texto.

3. Clique em 'Organizar Ficheiros' para começar a ordenar.

4. Uma mensagem de confirmação aparecerá quando terminar.""",
        "warning_title": "Aviso",
        "warning_text": "Por favor, selecione primeiro um diretório.",
        "confirm_title": "Confirmar",
        "confirm_text": "Tem a certeza que quer organizar os ficheiros em:\n%s?\n\nEsta ação não pode ser desfeita.",
        "error_title": "Erro",
        "error_text": "O diretório especificado não existe:\n%s",
        "completion_title": "Organização Concluída",
        "completion_log_message": "Organização concluída.\n\n%s",
        "completion_no_files_moved": "Nenhum ficheiro foi movido.",
        "moved_file_log": "Movido: %s -> %s/%s",
        "error_moving_file_log": "Erro ao mover %s: %s",
        "yes_button": "Sim",
        "no_button": "Não",
        "ok_button": "OK",
        "folder_name_template": "Arquivos %s",
    }
}
