import sys

import click

from .cat import cat, process


def read_stdin():
    """Read content from stdin"""
    return sys.stdin.read()


@click.command()
@click.argument('file_path')
def main(file_path):
    """Read from a file or stdin if file_path is '-'"""
    if file_path == '-':
        file_contents = read_stdin()
        click.echo(file_contents, nl=False)
    else:
        file_contents = cat(file_path)
        for chunk in file_contents:
            click.echo(process(chunk))


if __name__ == '__main__':
    main()
