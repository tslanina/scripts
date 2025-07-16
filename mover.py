import os
import shutil
import string

def get_target_folder(filename):
    first_char = filename[0].lower()
    if first_char in string.ascii_lowercase:
        return first_char
    else:
        return '0'

def main():
    current_dir = os.getcwd()

    for filename in os.listdir(current_dir):
        filepath = os.path.join(current_dir, filename)
        if not os.path.isfile(filepath):
            continue

        target_folder = get_target_folder(filename)
        target_path = os.path.join(current_dir, target_folder)
        os.makedirs(target_path, exist_ok=True)

        shutil.move(filepath, os.path.join(target_path, filename))

if __name__ == '__main__':
    main()
