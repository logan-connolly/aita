import typer

from .posts import ApiPosts
from .style import styled_count
from ..config import api_settings


app = typer.Typer()


@app.command()
def count():
    """Count number of AITA posts in database by label"""
    counts = ApiPosts(host=api_settings.host).count_labels()
    total = sum(count for _, count in counts)
    for label, count in counts:
        output = styled_count(label, count, total)
        typer.echo(output)
