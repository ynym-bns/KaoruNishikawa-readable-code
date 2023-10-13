#!/usr/bin/env python3

from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class DictEntry:
    """辞書ファイルに記載された単語とその読みを扱うクラス

    辞書ファイルには、単語とその読みがスペース区切りで記載されている。これを解釈し、`word` と `kana`
    プロパティでアクセスできるようにする。

    Examples:
        >>> entry = DictEntry("林檎 りんご")
        >>> entry.word
        '林檎'
        >>> entry.kana
        'りんご'

    """
    raw: str

    @property
    def word(self) -> str:
        return self.raw.split(" ")[0]
    
    @property
    def kana(self) -> str:
        return self.raw.split(" ")[1]
    
    def __str__(self) -> str:
        """f-string や print 文でインスタンスが直接参照された場合の挙動を定義
        
        f-string や print 文でインスタンスが直接参照された場合は、辞書ファイルの表記をそのまま返す。

        Examples:
            >>> entry = DictEntry("林檎 りんご")
            >>> print(entry)
            林檎 りんご
            >>> f"1: {entry}"
            '1: 林檎 りんご'
        
        """
        return self.raw


data_file_path = Path(__file__).parent / "dictionary-data.txt"


def print_dictionary(path: Path, index: Optional[int] = None) -> None:
    _data_file_contents = path.read_text()
    _data_file_contents = _data_file_contents.strip()  # 最終行が空行だった場合、その行を削除する
    _data_file_contents = _data_file_contents.splitlines()
    dict_data = [DictEntry(line) for line in _data_file_contents]

    if isinstance(index, int) and (0 < index <= len(dict_data)):
        entry = dict_data[index - 1]
        print(f"{index}: {entry.word} {entry.kana}")
    elif index is not None:
        # 与えられた index が単語IDの範囲外だった場合
        print(f"単語のIDは1から{len(dict_data)}までです。")
    else:
        for i, entry in enumerate(dict_data):
            print(f"{i + 1}: {entry.word} {entry.kana}")


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
