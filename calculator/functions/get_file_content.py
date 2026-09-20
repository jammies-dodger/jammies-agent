import os
from config import MAX_CHARS

def get_file_content(working_directory:str, file_path:str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        if not valid_target_file: return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            raise FileNotFoundError()

        file_content = ""
        with open(target_file, "r") as f:
            file_content = f.read(MAX_CHARS)
            # After reading the first MAX_CHARS...
            if f.read(1):
                file_content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        return file_content

    except FileNotFoundError:
        return f'Error: File not found or is not a regular file: "{file_path}"'
    except:
        return f'Error: Something went wrong while reading from "{file_path}"'
