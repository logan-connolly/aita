import typer

from aita.api.command import app as api_app
from aita.reddit.command import app as reddit_app
from aita.train.command import app as train_app


app = typer.Typer()
app.add_typer(api_app, name="api")
app.add_typer(reddit_app, name="reddit")
app.add_typer(train_app, name="train")


if __name__ == "__main__":
    app()
