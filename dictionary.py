#!/usr/bin/env python3

from dataclasses import dataclass
from pathlib import Path
from typing import Optional
import sys


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
        _raw_splitted_by_space = self.raw.split(" ")
        if len(_raw_splitted_by_space) > 1: # スペースで分割されていれば（配列外参照を懸念）
            return self.raw.split(" ")[1]
        else:
            return ""
    
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
    _data_file_contents = path.read_text(encoding="utf-8")
    _data_file_contents = _data_file_contents.strip()  # 最終行が空行だった場合、その行を削除する
    _data_file_contents = _data_file_contents.splitlines()
    dict_data = []
    current_user_index = -1 # ユーザー名が複数出た場合にそなえ、ユーザーをindexで管理する。
    for content in _data_file_contents:
        if "ユーザー名" in content:
            _, user_name = content.split() # ユーザー名と書かれた行を識別、最初のユーザー名：は不要でありアンダーバーで受け取る
            dict_data.append([user_name])
            current_user_index += 1
        else:
            if current_user_index == -1: # 配列に-1は渡せないので
                print("ユーザー名が見つかりませんでした")
                sys.exit() # 強制終了はよくないかもしれない
            
            dict_data[current_user_index].append(DictEntry(content))
    
    for user_content in dict_data:
        print(f'ユーザー名: {user_content[0]}')
        if isinstance(index, int) and (0 < index <= len(user_content)):
            entry = user_content[index - 1]
            print(f"{index}: {entry.word} {entry.kana}")
        elif index is not None:
            # 与えられた index が単語IDの範囲外だった場合
            print(f"単語のIDは1から{len(user_content)}までです。")
        else:
            for i in range(1, len(user_content)):
                entry = user_content[i]
                if entry.word != "" and entry.kana != "":
                    print(f"{i}: {entry.word} {entry.kana}")
        
        print() # 改行


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
