import typer

from .posts import ApiPosts
from ..config import api_settings
from ..style import whitespace


app = typer.Typer()


@app.command()
@whitespace(title="Number of AITA posts in DB:")
def count():
    """Count number of AITA posts in database by label"""
    counts = ApiPosts(host=api_settings.host).count_labels()
    total = sum(count for _, count in counts)
    for label, count in counts:
        typer.echo(styled_output(label, count, total))


def styled_output(label, count, total):
    fmt_label = typer.style(label, fg=typer.colors.WHITE, bold=True)
    fmt_count = typer.style(str(count), fg=typer.colors.BLUE)
    percent = round(count / total, 3)
    fmt_percent = typer.style(str(percent), fg=typer.colors.YELLOW)
    return f"{fmt_label}:\t {fmt_count}\t {fmt_percent}"
