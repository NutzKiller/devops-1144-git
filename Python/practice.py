import os
import time
import argparse

def list_old_files(directory_path, age_threshold_days):
    """
    List files older than a specified age threshold in a directory and its subdirectories.

    :param directory_path: The path of the directory to search for old files.
    :param age_threshold_days: The age threshold in days to consider files as old.
    """
    try:
        # Calculate the cutoff time
        cutoff_time = time.time() - (age_threshold_days * 86400)  # 86400 seconds in a day

        # Walk through the directory and its subdirectories
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                # Get the last modified time of the file
                file_mtime = os.path.getmtime(file_path)

                # Check if the file is older than the cutoff time
                if file_mtime < cutoff_time:
                    print(f"Old file: {file_path}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="List files older than a given age in days.")
    parser.add_argument("--directory",type=str, help="The path of the directory to search.")
    parser.add_argument("--age", type=int, help="The age threshold in days.")
    # parser.add_argument("--delete",type=str, help="To delete.")


    # Parse the arguments
    args = parser.parse_args()+

    # Call the function with the provided arguments
    list_old_files(args.directory, args.age)

if __name__ == "__main__":
    main()
