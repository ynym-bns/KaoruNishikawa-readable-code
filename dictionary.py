#!/usr/bin/env python3

from pathlib import Path


data_file_path = Path(__file__).parent / "dictionary-data.txt"

_data_file_contents = data_file_path.read_text()
dict_data = _data_file_contents.strip()  # 最終行が空行だった場合、その行を削除する

print(dict_data)
