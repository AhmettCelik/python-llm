import os


def get_files_info(working_directory, directory=None):
    try:
        absolute_path = os.path.abspath(directory)
        absolute_working_path = os.path.abspath(working_directory)
    except Exception:
        return f'Error: os.path.abspath throwing error: {Exception}'

    if not absolute_path.startswith(absolute_working_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(absolute_path):
        return f'Error: "{directory}" is not a directory'

    try:
        contents = os.listdir(absolute_path)
    except Exception:
        return f"Error: os.listdir throwing error: {Exception}"

    contents_data = {}

    for content in contents:
        try:
            content_path = os.path.join(absolute_path, content)
        except Exception:
            return f"Error: os.path.join throwing error: {Exception}"

        contents_data[content] = {}

        try:
            content_size = os.path.getsize(content_path)
        except Exception:
            return f"Error: os.path.getsize throwing error: {Exception}"

        contents_data[content]["file_size"] = content_size

        try:
            if os.path.isdir(content_path):
                contents_data[content]["is_dir"] = True
            else:
                contents_data[content]["is_dir"] = False
        except Exception:
            return f"Error: os.path.isdir throwing error: {Exception}"

    result_lines = []
    for content, data in contents_data.items():
        line = f"- {content}: file_size={data['file_size']
                                         } bytes, is_dir={data['is_dir']}"
        result_lines.append(line)

        result_string = "\n".join(result_lines)

    return result_string
