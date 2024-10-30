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

    if file_path:
        if file_path[0] == "-" and len(file_path) == 1:
            file_contents = cat()
            for chunk in file_contents:
                click.echo(chunk)
        else:
            for files in file_path:
                file_contents = cat(files)
                for chunk in file_contents:
                    click.echo(chunk, nl=False)
    else:
        file_contents = cat()
        for chunk in file_contents:
            chunk = chunk.split("\n")
            if number:
                for indx, content in enumerate(chunk, 1):
                    click.echo(f"     {indx}  {content}")

            if number_nonblank:
                indx = 1
                for content in chunk:
                    if content:
                        click.echo(f"     {indx}  {content}")
                        indx += 1
                    else:
                        click.echo()


if __name__ == "__main__":
    main()
