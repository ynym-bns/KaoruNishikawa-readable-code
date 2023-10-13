# KaoruNishikawa-readable-code

## 使用方法

1. リポジトリをクローンする

   ```shell
   git clone https://github.com/KaoruNishikawa/KaoruNishikawa-readable-code.git
   cd KaoruNishikawa-readable-code
   ```

2. プログラムを実行する

   ```shell
   ./dictionary.py
   ```

   > **note**  
   > 既定では [`dictionary.txt`](./dictionary-data.txt) に格納された辞書データが表示される。  
   > 以下のようにファイル名を追加して実行すれば、別の辞書ファイルを参照することもできる。
   >
   > ```shell
   > ./dictionary.py ./my-custom-dictionary.txt
   > ```
   >
   > ※ 辞書ファイルのフォーマットについては後述する。

   > **note**
   > 既定では辞書ファイルに格納された単語全てが表示される。  
   > 以下のように `-i` オプションを指定すれば、特定の単語のみ出力することができる。
   >
   > ```shell
   > # 単語ID=1の単語を表示する
   > ./dictionary.py -i 1
   >
   > # ./my-custom-dictionary.txt に記載された、単語ID=3の単語を表示する
   > ./dictionary.py ./my-custom-dictionary.txt -i 3
   > ```

## 辞書ファイルのフォーマット

辞書データは1行あたり1単語の情報を記述したテキストファイルで定義する。  
1単語の情報とは「単語」と「その読み仮名」のことで、半角スペースで区切って記述する。

なお、1行目に記載された単語は単語ID=1、2行目は単語ID=2のように、単語IDが自動的に設定される。

ユーザー名から始まる行は関連するユーザー名を示す。
最初の行はユーザー名から始まるものとする。

```text
ユーザー名: kou
上手 じょうず
一時 いちじ
市場 しじょう
```
