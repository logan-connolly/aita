from collections import Counter

import typer

from ..style import whitespace


@whitespace(title="Number of AITA posts added to DB:")
def styled_add(counter: Counter) -> None:
    """Format text output to print out to console.
    :param counter: Counter object from collections
    """
    new_posts = typer.style("new post:", fg=typer.colors.GREEN)
    existed = typer.style("existed:", fg=typer.colors.RED)
    ignored = typer.style("ignored:", fg=typer.colors.YELLOW)
    errors = typer.style("errors: ", fg=typer.colors.BRIGHT_RED)
    typer.echo(f"{new_posts}\t {counter['added']}")
    typer.echo(f"{existed}\t {counter['existed']}")
    typer.echo(f"{ignored}\t {counter['ignored']}")
    typer.echo(f"{errors}\t {counter['error']}")
