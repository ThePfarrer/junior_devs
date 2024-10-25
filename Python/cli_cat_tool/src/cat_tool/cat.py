def process(chunk):
    text = chunk.decode('utf-8')
    return text


def cat(file_path):
    try:
        chunk_size = 1024
        with open(file_path, 'rb') as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                yield chunk
    except FileNotFoundError:
        return f"Error: No file found in {file_path}"
    except IOError:
        return f"Error: There was an issue reading the file {file_path}"

