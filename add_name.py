import os
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python change_name.py <target_folder>")
        sys.exit(1)

    folder_path = sys.argv[1]

    for filename in os.listdir(folder_path):
        if filename.startswith("hust_") and filename.endswith(".md"):
            parts = filename.split("_")
            new_filename = f"hust_ts_{parts[1]}_" + "_".join(parts[2:])
            os.rename(
                os.path.join(folder_path, filename),
                os.path.join(folder_path, new_filename),
            )

if __name__ == "__main__":
    main()