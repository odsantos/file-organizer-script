#!/bin/bash

# Configuration for fileorganizer.odsantos.com
PROJECT_NAME="fileorganizer.odsantos.com"
LOCAL_DIR="/var/www/osvaldo/fileorganizer.odsantos.com/"
REMOTE_DIR="/home/odsaophq/fileorganizer.odsantos.com"

# Call the centralized deployment script
/var/www/osvaldo/scripts/deploy.sh "$LOCAL_DIR" "$REMOTE_DIR" "$PROJECT_NAME"
