import os

def get_files_info(working_directory: str, directory:str = ".") -> str:

    output = f"Result for {"current" if directory == "." else directory} directorytimesheet:\n\t"
                
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        if not os.path.isdir(target_dir):
            raise NotADirectoryError()
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    except NotADirectoryError:
        return f'{output}Error: "{directory}" is not a directory'
    except:
        return f'{output}Error: Something went wrong while validating the target directory'
    else:
        if not valid_target_dir: return f'{output}Error: Cannot list "{directory}", as it is outside the permitted working directory'
        else: 
            
            try:
                for item in os.listdir(target_dir):
                    item_path = os.path.normpath(os.path.join(target_dir, item))
                    is_dir = os.path.isdir(item_path)
                    file_size = os.path.getsize(item_path)
                    output += f"- {item}: file_size={file_size} bytes, is_dir={is_dir}\n\t"
                
                return output
            except:
                return f'{output}Error: Something went wrong while inspecting items in target directory {target_dir}'
            # return f'Success: "{directory}" is within the working directory'