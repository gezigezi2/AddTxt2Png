# AddTxt2Png
概要
pngファイルの右下に小さく任意のテキストを書き込んで保存します。
同時に画像に含まれる余計な情報(プロンプトなど)を削除します。
AI生成画像に署名を入れたりするのに便利です。

使い方
PythonがインストールされているPCで動作します。
ソースコード内の
"Write text here.ここに右下に追加するテキストを書きます"
の部分に書き込みたい文字を記入します。

フォルダを作り、署名を入れたいファイルをその中に入れ、ファイル名の先頭にアンダーバー"_"を付けます。
このプログラムは先頭に"_"が付いたpngファイルだけテキストを書き込みます。
フォルダの下にさらにフォルダがある場合でも全てのファイルを自動探索して全て書き込みます。

このソースコード”AddTxt2Png.py”を処理したい画像のあるフォルダの中に入れ
(通常のインストール方法でpytonが入っている場合は)ダブルクリックで実行します。

処理済みのファイルは元のファイル名の先頭に#を付けた状態で保存されます。
(もし、偶然同じ名前のファイルがある場合上書きされるので注意してください)
かなり再帰探索が強力なので、何回か動作テストを行ってから使ってください。

gezigezi