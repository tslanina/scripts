import os
import zlib
import shutil

def calculate_crc32(filepath, chunk_size=65536):
    crc = 0
    with open(filepath, 'rb') as f:
        while chunk := f.read(chunk_size):
            crc = zlib.crc32(chunk, crc)
    return format(crc & 0xFFFFFFFF, '08x')

def main():
    current_dir = os.getcwd()
    duped_dir = os.path.join(current_dir, 'duped')
    os.makedirs(duped_dir, exist_ok=True)

    seen_crcs = {}
    file_count = 0
    dup_count = 0

    for filename in os.listdir(current_dir):
        filepath = os.path.join(current_dir, filename)
        if not os.path.isfile(filepath):
            continue

        crc = calculate_crc32(filepath)
        if crc not in seen_crcs:
            seen_crcs[crc] = filepath
        else:
            shutil.move(filepath, os.path.join(duped_dir, filename))
            dup_count += 1

        file_count += 1
        if file_count % 1000 == 0:
            print(f"Processed {file_count} files...")

    print(f"Done. Moved {dup_count} duplicates to 'duped' folder.")

if __name__ == '__main__':
    main()
