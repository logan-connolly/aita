import typer

from .posts import ApiPosts
from ..style import whitespace


app = typer.Typer()


@app.command()
@whitespace(title="Number of AITA posts in DB:")
def count():
    """Count number of AITA posts in database by label"""
    counts = ApiPosts(host="api:8000").count_labels()
    total = sum(count for _, count in counts)
    for label, count in counts:
        typer.echo(_styled_count(label, count, total))


def _styled_count(label, count, total):
    label_styled = typer.style(label, fg=typer.colors.WHITE, bold=True)
    count_styled = typer.style(str(count), fg=typer.colors.BLUE)
    percent = round(count / total, 3)
    pct_styled = typer.style(str(percent), fg=typer.colors.YELLOW)
    return f"{label_styled}:\t {count_styled}\t {pct_styled}"
