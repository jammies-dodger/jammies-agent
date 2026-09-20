import os
import subprocess

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Execute/Run Python file with optional arguments, py file specified relative to the working directory, providing any non zero exit code then stdout and stderr output if there are any",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to execute python from, relative to the working directory (default is the working directory itself)",
                },
                "args": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    },
                    "description": "Optional arguments that will be passed to the python subprocess if there are any",
                },
            },
            "required": ["file_path"]
        },
    },
}

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        if not valid_target_file: return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_file]
        if args:
            command.extend(args)

        result: subprocess.CompletedProcess = subprocess.run(command, cwd=working_dir_abs, capture_output=True, text=True, timeout=30)

        output: list[str] = []
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        if not result.stderr and not result.stdout:
            output.append("No output produced")
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")
        return "\n".join(output)
    except Exception as e:
        return f"Error: executing Python file: {e}"