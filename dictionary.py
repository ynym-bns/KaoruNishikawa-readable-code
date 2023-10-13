#!/usr/bin/env python3

from pathlib import Path


data_file_path = Path(__file__).parent / "dictionary-data.txt"


def print_dictionary(path: Path) -> None:
    _data_file_contents = data_file_path.read_text()
    dict_data = _data_file_contents.strip()  # 最終行が空行だった場合、その行を削除する

    for i, line in enumerate(dict_data.splitlines()):
        print(f"{i + 1}: {line}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "file",
        help="辞書データが格納されたファイルのパス",
        default=str(data_file_path),
        nargs="?",
    )

    args = parser.parse_args()

    print_dictionary(Path(args.file))
