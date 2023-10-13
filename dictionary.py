#!/usr/bin/env python3

from pathlib import Path
from typing import Optional


data_file_path = Path(__file__).parent / "dictionary-data.txt"


def print_dictionary(path: Path, index: Optional[int] = None) -> None:
    _data_file_contents = path.read_text()
    _data_file_contents = _data_file_contents.strip()  # 最終行が空行だった場合、その行を削除する
    dict_data = _data_file_contents.splitlines()

    if isinstance(index, int) and (0 < index <= len(dict_data)):
        print(f"{index}: {dict_data[index - 1]}")
    elif index is not None:
        # 与えられた index が単語IDの範囲外だった場合
        print(f"単語のIDは1から{len(dict_data)}までです。")
    else:
        for i, line in enumerate(dict_data):
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
    parser.add_argument(
        "--index", "-i", type=int, help="表示する単語のID", required=False
    )

    args = parser.parse_args()

    print_dictionary(Path(args.file), args.index)
