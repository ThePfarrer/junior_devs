import click

from .cat import cat


@click.command()
@click.argument('file_path')
def main(file_path):
    """Read the file to the CLI"""
    file_contents = cat(file_path)
    print(file_contents)


if __name__ == '__main__':
    main()
