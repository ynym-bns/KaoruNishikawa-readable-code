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

## 辞書ファイルのフォーマット

辞書データは1行あたり1単語を記述したテキストファイルで定義する。

```text
上手
一時
市場
```
