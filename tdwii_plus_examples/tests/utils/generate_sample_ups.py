import sys

from tdwii_plus_examples.tests.utils.generate_sop_instances import generate_ups_file


def main():
    if len(sys.argv) not in (2, 3):
        print("Usage: python generate_sample_ups.py <folder_path> [file_name]")
        sys.exit(1)
    folder_path = sys.argv[1]
    file_name = sys.argv[2] if len(sys.argv) == 3 else None
    file_path = generate_ups_file(folder_path, file_name)
    print(f"Sample UPS file succesfully created: {file_path}")


if __name__ == "__main__":
    main()
