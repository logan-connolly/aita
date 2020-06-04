import typer


def styled_count(label: str, count: int, total: int) -> str:
    """Stylize output to be printed to console.
    :param label: contains AITA flair label
    :param count: how many exist in database
    :param total: total amount of AITA items in database
    """
    fmt_label = typer.style(label, fg=typer.colors.WHITE, bold=True)
    fmt_count = typer.style(str(count), fg=typer.colors.BLUE)
    percent = round(count / total, 3)
    fmt_percent = typer.style(str(percent), fg=typer.colors.YELLOW)
    return f"{fmt_label}:\t {fmt_count}\t {fmt_percent}"
