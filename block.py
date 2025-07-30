import os
import argparse

def scan_files(extension, block_size_bytes):
    print(f"Scanning for '*.{extension}' files not aligned to {block_size_bytes} byte blocks...\n")

    for root, _, files in os.walk('.'):
        for file in files:
            if file.lower().endswith(f".{extension.lower()}"):
                filepath = os.path.join(root, file)
                try:
                    filesize = os.path.getsize(filepath)
                    remainder = filesize % block_size_bytes
                    if remainder != 0:
                        print(f"File: {filepath}")
                        print(f" - Size: {filesize} bytes")
                        print(f" - Size mod {block_size_bytes} bytes: {remainder} bytes\n")
                except Exception as e:
                    print(f"Error reading {filepath}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scan files and check size alignment.")
    parser.add_argument("extension", help="File extension to search for (e.g., txt)")
    parser.add_argument("block_size_bytes", type=int, help="Block size in bytes to check alignment (e.g., 4096)")
    args = parser.parse_args()

    scan_files(args.extension, args.block_size_bytes)
