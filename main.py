"""Mainn uc is yapar: argumanlari oku, hatti kur, run() cagir."""
import sys

from logflow.console_sink import ConsoleSink
from logflow.file_line_source import FileLineSource
from logflow.pipeline import Pipeline


def main(argv: list) -> int:
    if len(argv) != 2:
        print("Kullanim: python main.py <log-dosyasi>", file=sys.stderr)
        return 2
    try:
        Pipeline(FileLineSource(argv[1]), ConsoleSink()).run()
    except Exception as e:
        print(f"Hata: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
