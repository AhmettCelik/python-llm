import os


def get_files_info(working_directory, directory=None):
    try:
        absolute_path = os.path.abspath(directory)
        absolute_working_path = os.path.abspath(working_directory)
    except Exception as e:
        return f'Error: os.path.abspath throwing error: {e}'

    directory = os.path.join(working_directory, directory)
    absolute_directory = os.path.abspath(directory)

    print(absolute_path)
    print(absolute_working_path)
    print(directory)
    print(absolute_directory)

    if not absolute_path.startswith(absolute_working_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(absolute_path):
        return f'Error: "{directory}" is not a directory'

    try:
        contents = os.listdir(absolute_path)
    except Exception as e:
        return f"Error: os.listdir throwing error: {e}"

    contents_data = {}

    try:
        for content in contents:
            content_path = os.path.join(absolute_path, content)
            contents_data[content] = {}
            content_size = os.path.getsize(content_path)
            contents_data[content]["file_size"] = content_size

            if os.path.isdir(content_path):
                contents_data[content]["is_dir"] = True
            else:
                contents_data[content]["is_dir"] = False
    except Exception as e:
        return f"Error: an error occured in contents list for loop {e}"

    result_lines = []
    for content, data in contents_data.items():
        line = f"- {content}: file_size={data['file_size']
                                         } bytes, is_dir={data['is_dir']}"
        result_lines.append(line)

        result_string = "\n".join(result_lines)

    return result_string
