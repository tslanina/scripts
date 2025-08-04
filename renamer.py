import os
import sys

base = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890()[]!_"

def normalize_filename(filename, base):
    name, ext = os.path.splitext(filename)
    normalized = ''.join(char if char in base else '_' for char in name)
    return normalized + ext

def get_unique_filename(directory, filename):
    base_name, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(os.path.join(directory, new_filename)):
        new_filename = f"{base_name}{counter}{ext}"
        counter += 1
    return new_filename

def rename_files_in_directory(base, extension):
    current_dir = os.getcwd()
    for filename in os.listdir(current_dir):
        if filename.endswith(extension):
            normalized = normalize_filename(filename, base)
            if normalized != filename:
                unique_name = get_unique_filename(current_dir, normalized)
                os.rename(os.path.join(current_dir, filename),
                          os.path.join(current_dir, unique_name))
                print(f"Name change: {filename} → {unique_name}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a file extension (without the dot) as a script argument.")
        print("Example: python renamer.py smc")
        sys.exit(1)

    extension = "." + sys.argv[1]
    rename_files_in_directory(base, extension)
