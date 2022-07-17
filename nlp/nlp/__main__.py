import sys
from typing import Optional, Sequence

from nlp import cli


def main(argv: Optional[Sequence[str]] = None) -> None:
    """Command interface for aita nlp command line utility"""

    args = cli.parse_args(argv)

    if args.command == cli.Command.DOWNLOAD.value:
        cli.download(args.url)

    elif args.command == cli.Command.PREPROCESS.value:
        cli.preprocess(args.id, args.labels)

    elif args.command == cli.Command.TRAIN.value:
        cli.train(args.id)

    else:
        raise ValueError("Invalid command passed.")


if __name__ == "__main__":
    main(sys.argv[1:])
