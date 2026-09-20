import os

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Write or overwrite file, file specified relative to the working directory, provides number of characters written",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to write to or create, relative to the working directory (default is the working directory itself)",
                },
                "content": {
                    "type": "string",
                    "description": "Content to write to given file, this will overwrite previous content",
                },
            },
            "required": ["file_path", "content"]
        },
    },
}

def write_file(working_directory:str, file_path:str, content: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        if not valid_target_file: return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        os.makedirs(os.path.dirname(target_file), exist_ok=True)

        with open(target_file, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except:
        return f'Error: Something went wrong while writing to "{file_path}"'