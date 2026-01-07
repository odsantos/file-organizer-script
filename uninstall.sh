#!/bin/bash

echo "Uninstalling File Organizer..."

# Define user-local installation paths
INSTALL_DIR_BIN="$HOME/.local/bin"
INSTALL_DIR_DESKTOP="$HOME/.local/share/applications"
INSTALL_DIR_ICONS="$HOME/.local/share/icons/hicolor/scalable/apps"

# Remove files
echo "Removing executable from $INSTALL_DIR_BIN/file-organizer"
rm -f "$INSTALL_DIR_BIN/file-organizer"

echo "Removing icon from $INSTALL_DIR_ICONS/file-organizer.png"
rm -f "$INSTALL_DIR_ICONS/file-organizer.png"

echo "Removing desktop entry from $INSTALL_DIR_DESKTOP/file-organizer.desktop"
rm -f "$INSTALL_DIR_DESKTOP/file-organizer.desktop"

# Refresh the desktop database
echo "Updating desktop database..."
update-desktop-database "$INSTALL_DIR_DESKTOP"

echo ""
echo "Uninstallation complete!"
