import typer

from .posts import ApiPosts
from .style import styled_count
from ..style import whitespace


app = typer.Typer()


@app.command()
@whitespace(title="Number of AITA posts in DB:")
def count(host: str):
    """Count number of AITA posts in database by label"""
    counts = ApiPosts(host).count_labels()
    if not counts:
        typer.echo("No posts found in DB")
    else:
        total = sum(count for _, count in counts)
        for label, count in counts:
            output = styled_count(label, count, total)
            typer.echo(output)
