import click

from .cat import cat


class CounterClass:
    def __init__(self):
        self.counter = 1

    def increment(self):
        self.counter += 1


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

    line_number = CounterClass()

    if not file_path or (file_path == ("-",)):
        file_contents = cat()
        for chunk in file_contents:
            display_with_line_numbers(chunk, line_number, number, number_nonblank)
    else:
        for files in file_path:
            output_file_contents(files, line_number, number, number_nonblank)


def display_with_line_numbers(content, counter, number=False, number_nonblank=False):
    """
    Display content with line numbers if specified.
    """
    lines = content.split("\n")
    for line in lines:
        line_number_format = str(counter.counter).rjust(6, " ")
        if number:
            click.echo(f"{line_number_format}  {line}")
            counter.increment()

        elif number_nonblank:
            if line:
                click.echo(f"{line_number_format}  {line}")
                counter.increment()
            else:
                click.echo()
        else:
            click.echo(line)


def output_file_contents(file_path, counter, number, number_nonblank):
    """
    Outputs the contents of a file, with optional line numbering.
    """
    file_contents = cat(file_path)
    for chunk in file_contents:
        display_with_line_numbers(chunk, counter, number, number_nonblank)


if __name__ == "__main__":
    main()
