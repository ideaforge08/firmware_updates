import json
import hashlib

# Function to calculate checksum for a file
def calculate_checksum(file_path):
    with open(file_path, "rb") as file:
        file_content = file.read()
        checksum = hashlib.sha256(file_content).hexdigest()
    return checksum

# Define metadata for Version 1.txt
file_name = "Version 1.txt"
version = "1.0"  # You can automate this if you have a versioning scheme
checksum = calculate_checksum(file_name)
description = f"Metadata for {file_name}"

# Construct metadata dictionary for Version 1.txt
file_metadata = {
    file_name: {
        "version": version,
        "checksum": checksum,
        "description": description
    }
}

# Specify the path for the metadata file
metadata_file = "metadata 1.json"

# Write metadata to JSON file
with open(metadata_file, "w") as json_file:
    json.dump(file_metadata, json_file, indent=4)

print("Metadata file created successfully.")
