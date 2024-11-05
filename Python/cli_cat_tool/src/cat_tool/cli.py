import click

from .cat import cat


@click.command()
@click.option("-n", "number", is_flag=True, help="number all output lines")
@click.option(
    "-b",
    "number_nonblank",
    is_flag=True,
    help="number nonempty output lines, overrides -n",
)
@click.argument("file_path", nargs=-1)
def main(number, number_nonblank, file_path):
    """
    Concatenate FILE(s) to standard output.

    With no FILE, or when FILE is -, read standard input.
    """

    if not file_path or (file_path == ("-",)):
        file_contents = cat()
        for chunk in file_contents:
            display_with_line_numbers(chunk, number, number_nonblank)
    else:
        for files in file_path:
            output_file_contents(files, number, number_nonblank)


def display_with_line_numbers(content, number=False, number_nonblank=False):
    """
    Display content with line numbers if specified.
    """
    lines = content.split("\n")
    line_number = 1
    for line in lines:
        if number:
            click.echo(f"     {line_number}  {line}")
            line_number += 1

        elif number_nonblank:
            if line:
                click.echo(f"     {line_number}  {line}")
                line_number += 1
            else:
                click.echo()
        else:
            click.echo(line)


def output_file_contents(file_path, number, number_nonblank):
    """
    Outputs the contents of a file, with optional line numbering.
    """
    file_contents = cat(file_path)
    for chunk in file_contents:
        display_with_line_numbers(chunk, number, number_nonblank)


if __name__ == "__main__":
    main()
