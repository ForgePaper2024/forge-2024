import json
import os

def list_files_in_directory(directory_path):
    file_paths = []

    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            
            file_path = os.path.join(root, file_name)
            file_paths.append(file_path)

    return file_paths

def extract_name_from_path(file_path):
    base_name = os.path.basename(file_path)
    name_without_extension = os.path.splitext(base_name)[0]
    return name_without_extension

def remove_and_check_duplicates(file_paths):
    repo_sizes = []
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            data = json.load(file)

        ids = [element['id'] for element in data]

        duplicate_ids = set()
        seen_ids = set()
        indices_to_remove = []
        for i, id_value in enumerate(ids):
            if id_value in seen_ids:
                duplicate_ids.add(id_value)
                indices_to_remove.append(i)
            else:
                seen_ids.add(id_value)

        name = extract_name_from_path(file_path)

        if duplicate_ids:
            print(f"Duplicate IDs found {name}: {duplicate_ids}")

            # Remove one instance of each duplicate from the original list
            for index_to_remove in reversed(indices_to_remove):
                del data[index_to_remove]

            with open(file_path, 'w') as file:
                name = extract_name_from_path(file_path)
                repos = f"{name} - {len(data)}"
                repo_sizes.append(repos)
                json.dump(data, file, indent=2)

            print(f"Duplicates for {name} removed.")
        else:
            print(f"No duplicate IDs found for {name}.")
    for repo in repo_sizes:
        print(repo)

if __name__ == '__main__':
    directory_path = 'strong_copyleft'
    files_in_directory = list_files_in_directory(directory_path)
    remove_and_check_duplicates(files_in_directory)