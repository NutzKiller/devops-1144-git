def count_files(directory):
    file_count = 0
    for root, dirs, files in os.walk(directory):
        file_count += len(files)
    return file_count

directory = '/path/to/directory'
print(count_files(directory))