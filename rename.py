import os
import sys

def normalize_filename(filename, existing_names):
    name, ext = os.path.splitext(filename)
    normalized_name = ''.join('_' if not c.isascii() else c for c in name)
    
    counter = 1
    new_name = normalized_name
    while new_name + ext in existing_names:
        new_name = f"{normalized_name}_{counter}"
        counter += 1

    existing_names.add(new_name + ext)
    return new_name + ext

def rename_files_in_directory(extension):
    directory = os.getcwd()  # Pobiera aktualny katalog
    existing_names = set()
    
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            existing_names.add(filename)
    
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath) and filename.endswith(extension):
            if any(not c.isascii() for c in filename):
                new_filename = normalize_filename(filename, existing_names)
                new_filepath = os.path.join(directory, new_filename)
                print(f"Zmiana: {filename} -> {new_filename}")
                os.rename(filepath, new_filepath)

# Sprawdzenie argumentu wywołania
if len(sys.argv) != 2:
    print("Użycie: python script.py .rozszerzenie")
    sys.exit(1)

file_extension = sys.argv[1]
rename_files_in_directory(file_extension)
