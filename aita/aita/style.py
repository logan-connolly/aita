import functools

import typer


def whitespace(title: str = None):
    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            typer.echo()
            if title:
                title_fmt = typer.style(title, bold=True)
                typer.echo(f"{title_fmt}\n")
            func(*args, **kwargs)
            typer.echo()

        return inner

    return decorator
