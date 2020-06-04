import typer

from ..api.posts import ApiPosts


app = typer.Typer()


@app.command()
def train(host: str):
    """Count number of AITA posts in database by label"""
    data = ApiPosts(host).posts()
    typer.echo(data[0])
