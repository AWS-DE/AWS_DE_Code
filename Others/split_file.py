import os

def split_file(file_path, file_name, part_size):
    # Get the base file name without the path
    file_name = os.path.basename(file_path + file_name)
    # Determine the size of the file
    file_size = os.path.getsize(file_path + file_name)
    # Calculate the number of parts needed
    part_count = (file_size + part_size - 1) // part_size
    
    with open(file_path + file_name, 'rb') as f:
        for i in range(part_count):
            part_file_name =  f"{file_path}{file_name}.part{i+1}"
            with open(part_file_name, 'wb') as part_file:
                part_file.write(f.read(part_size))
                print(f"Created {part_file_name}")

if __name__ == "__main__":
    # Define the file path and the part size in bytes
    file_path = 'D:\\AWS Data Engineer\\awsde-materials\\code\\s3\\Multi Part\\'
    file_name = '07_1_AWS_s3_revision.mp4'
    part_size = 10 * 1024 * 1024  # 10 MB
    split_file(file_path, file_name, part_size)
