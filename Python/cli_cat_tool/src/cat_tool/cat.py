def cat(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return f"Error: No file found in {file_path}"
    except IOError:
        return f"Error: There was an issue reading the file {file_path}"
