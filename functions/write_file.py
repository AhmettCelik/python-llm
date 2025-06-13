import os
from functions.get_file_content import get_file_content


def write_file(working_directory, file_path, content):
    full_path = os.path.join(working_directory, file_path)

    if not os.path.exists(full_path):
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        open(full_path, "w").close()

    file_content = get_file_content(working_directory, file_path)
    if file_content.startswith("Error:"):
        return file_content

    try:
        with open(full_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
