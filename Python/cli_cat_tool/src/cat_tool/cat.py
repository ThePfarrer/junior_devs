import sys


def cat(file_path=None):
    try:
        chunk_size = 1024
        if file_path:
            with open(file_path, "r") as file:
                while True:
                    chunk = file.read(chunk_size).rstrip()
                    if not chunk:
                        break
                    yield chunk
        else:
            while True:
                chunk = sys.stdin.read(chunk_size).rstrip()
                if not chunk:
                    break
                yield chunk

    except FileNotFoundError:
        yield f"Error: No file found in {file_path}"
    except IOError:
        yield f"Error: There was an issue reading the file {file_path}"
