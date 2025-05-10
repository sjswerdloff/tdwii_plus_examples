import sys

from tdwii_plus_examples.tests.utils.generate_sop_instances import generate_ups_file


def main():
    if len(sys.argv) != 2:
        print("Usage: python create_sample_ups.py <folder_path>")
        sys.exit(1)
    folder_path = sys.argv[1]
    generate_ups_file(folder_path)
    print(f"Sample UPS file created in: {folder_path}")


if __name__ == "__main__":
    main()
