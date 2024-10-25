import sys

import click

from .cat import cat, process


def read_stdin():
    """Read content from stdin"""
    return sys.stdin.read().rstrip()


@click.command()
@click.option('-n', is_flag=True)
@click.argument('file_path', nargs=-1)
def main(n, file_path):
    """Read from a file or stdin if file_path is '-'"""
    if n:
        file_contents = read_stdin().split("\n")
        for indx, content in enumerate(file_contents, 1):
            click.echo(f"{indx} {content}")
    if file_path == '-':
        file_contents = read_stdin()
        click.echo(file_contents)
    else:
        for files in file_path:
            file_contents = cat(files)
            for chunk in file_contents:
                click.echo(process(chunk), nl=False)


if __name__ == '__main__':
    main()
