import sys

def convert_bin_to_text(input_file, output_file):
    """Convert a binary file to a text file formatted for Z80 assembly."""
    try:
        with open(input_file, "rb") as bin_file, open(output_file, "w") as txt_file:
            while chunk := bin_file.read(32):  # Read up to 32 bytes at a time
                hex_values = ", ".join(f"${byte:02x}" for byte in chunk)  # Convert to lowercase hex format
                txt_file.write(f"db {hex_values}\n")  # Write in assembly format
        print(f"Conversion complete. Output file: {output_file}")
    except FileNotFoundError:
        print("Error: Input file not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file.bin> <output_file.txt>")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    convert_bin_to_text(input_filename, output_filename)
