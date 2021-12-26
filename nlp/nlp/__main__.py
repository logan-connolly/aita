import sys
from typing import Optional, Sequence

from nlp import cli


def main(argv: Optional[Sequence[str]] = None) -> None:
    """Command interface for aita nlp command line utility"""

    args = cli.parse_args(argv)
    validated_args = cli.validate_args(args)

    if validated_args.command == "download":
        cli.download(validated_args.url)

    if validated_args.command == "preprocess":
        cli.preprocess(validated_args.id, validated_args.labels)

    if validated_args.command == "train":
        cli.train(validated_args.id)


if __name__ == "__main__":
    main(sys.argv[1:])
