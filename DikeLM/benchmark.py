import os

def find_small_files(folder_path, threshold_gb):
    threshold_bytes = threshold_gb * (1024 ** 3) 
    small_files = []

    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            try:
                file_size = os.path.getsize(file_path)
                if file_size < threshold_bytes:
                    small_files.append(os.path.abspath(file_path))
            except OSError:
                pass
    return small_files

# folder_path = 
# threshold_gb = 1