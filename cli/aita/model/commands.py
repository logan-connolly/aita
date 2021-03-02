import typer

from ..api.posts import ApiPosts

app = typer.Typer()


@app.command()
def train(host: str):
    """Count number of AITA posts in database by label"""
    data = ApiPosts(host).posts()
    if data:
        typer.echo(data[0])
    else:
        typer.echo("No data")
