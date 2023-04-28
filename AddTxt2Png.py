import os
from PIL import Image, ImageDraw, ImageFont

# 処理するフォルダのパスを指定する
folder_path = "./"

# フォルダ以下のすべての画像ファイルを検索して、処理を適用する
for dirpath, dirnames, filenames in os.walk(folder_path):
    for filename in filenames:
        if not filename.endswith(".png"):
            continue
        if filename.startswith("_"):
            # 画像ファイルを読み込む
            image_path = os.path.join(dirpath, filename)
            with Image.open(image_path) as image:
                draw = ImageDraw.Draw(image)

                # テキストを描画する
                text = "Write text here.ここに右下に追加するテキストを書きます"
                #font = ImageFont.truetype("arial.ttf", 16)#英語だけで良い場合
                font = ImageFont.truetype('C:\Windows\Fonts\meiryo.ttc', 16)#日本語を含む場合
                text_width, text_height = draw.textsize(text, font)
                x = image.width - text_width
                y = image.height - text_height
                draw.text((x, y), text, font=font, fill=(255, 255, 255, 255))

                # プロンプト情報を削除する
                image.info = {}
                # 画像を保存する
                new_filename = "#" + filename
                new_image_path = os.path.join(dirpath, new_filename)
                image.save(new_image_path)

                print(f"Saved new image to {new_image_path}")
