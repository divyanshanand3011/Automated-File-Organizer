import os
import shutil
from datetime import datetime

# Project: Automated File Organizer
# Language: Python

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Python_Files": [".py"],
    "Archives": [".zip", ".rar", ".7z"],
    "Code_Files": [".html", ".css", ".js", ".cpp", ".java"]
}


def create_folder(path):
    """Create a folder if it does not exist."""
    os.makedirs(path, exist_ok=True)


def get_category(extension):
    """Identify the category of a file."""
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category

    return "Others"


def organize_files(source_folder):
    """Organize files according to their extensions."""

    if not os.path.isdir(source_folder):
        print("Error: Source folder does not exist!")
        return

    print("\n" + "=" * 45)
    print("       AUTOMATED FILE ORGANIZER")
    print("=" * 45)
    print("Started at:", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

    summary = {}
    moved_count = 0
    skipped_count = 0

    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        # Skip directories
        if not os.path.isfile(source_path):
            continue

        # Get file extension
        extension = os.path.splitext(filename)[1]

        # Find category
        category = get_category(extension)

        # Create destination folder
        destination_folder = os.path.join(
            source_folder, category
        )
        create_folder(destination_folder)

        destination_path = os.path.join(
            destination_folder, filename
        )

        # Avoid overwriting existing files
        if os.path.exists(destination_path):
            print(f"Skipped: {filename} (already exists)")
            skipped_count += 1
            continue

        try:
            shutil.move(source_path, destination_path)

            print(f"Moved: {filename} -> {category}/")

            summary[category] = summary.get(category, 0) + 1
            moved_count += 1

        except OSError as error:
            print(f"Error moving {filename}: {error}")

    print("\n" + "=" * 45)
    print("             FINAL REPORT")
    print("=" * 45)

    for category, count in sorted(summary.items()):
        print(f"{category}: {count} file(s)")

    print("-" * 45)
    print("Total files moved:", moved_count)
    print("Total files skipped:", skipped_count)
    print("Completed at:", datetime.now().strftime("%H:%M:%S"))
    print("=" * 45)


if __name__ == "__main__":
    folder_path = input(
        "\nEnter the folder path to organize: "
    ).strip().strip('"')

    organize_files(folder_path)