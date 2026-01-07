#!/bin/bash

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Define user-local installation paths
INSTALL_DIR_BIN="$HOME/.local/bin"
INSTALL_DIR_DESKTOP="$HOME/.local/share/applications"
INSTALL_DIR_ICONS="$HOME/.local/share/icons/hicolor/scalable/apps"

# Create directories if they don't exist
mkdir -p "$INSTALL_DIR_BIN"
mkdir -p "$INSTALL_DIR_DESKTOP"
mkdir -p "$INSTALL_DIR_ICONS"

echo "Installing File Organizer..."

# Copy executable
echo "Installing executable to $INSTALL_DIR_BIN/file-organizer"
cp "$SCRIPT_DIR/File Organizer" "$INSTALL_DIR_BIN/file-organizer"
chmod +x "$INSTALL_DIR_BIN/file-organizer"

# Copy icon
# The icon is located relative to the executable in the build artifact
echo "Installing icon to $INSTALL_DIR_ICONS/file-organizer.png"
cp "$SCRIPT_DIR/assets/images/icon-1024x1024.png" "$INSTALL_DIR_ICONS/file-organizer.png"

# Copy .desktop file
echo "Installing desktop entry to $INSTALL_DIR_DESKTOP/file-organizer.desktop"
cp "$SCRIPT_DIR/file-organizer.desktop" "$INSTALL_DIR_DESKTOP/file-organizer.desktop"

# Refresh the desktop database
echo "Updating desktop database..."
update-desktop-database "$INSTALL_DIR_DESKTOP"

echo ""
echo "Installation complete!"
echo "You can now launch 'File Organizer' from your application menu."
echo "You might need to log out and log back in for the icon to appear correctly."
