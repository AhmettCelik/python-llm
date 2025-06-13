import os
import functions


def write_file(working_directory, file_path, content):
    file_content = functions.get_file_content(working_directory, file_path)
    if file_content.startswith("Error:"):
        return file_content
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    try:
        with open(file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
