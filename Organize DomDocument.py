import os
import re

BASE_DIR = os.path.dirname(__file__)

MEDIA_DIR = os.path.join(BASE_DIR, "Library", "media")
IMAGE_DIR = os.path.join(BASE_DIR, "Library", "image")
SPRITE_DIR = os.path.join(BASE_DIR, "Library", "sprite")
LABEL_DIR = os.path.join(BASE_DIR, "Library", "label")

DOM_FILE = os.path.join(BASE_DIR, "DOMDocument.xml")


def GenerateMedia():
    lanes = ["    <media>"]

    files = sorted(f for f in os.listdir(MEDIA_DIR) if f.endswith(".png"))

    for file in files:
        name = file[:-4]
        lanes.append(
            f'        <DOMBitmapItem name="media/{name}" href="media/{file}"/>'
        )

    lanes.append("    </media>")
    return "\n".join(lanes)


def GenerateSymbols():
    lanes = ["    <symbols>"]

    def add(folder, prefix):
        files = sorted(f for f in os.listdir(folder) if f.endswith(".xml"))
        for file in files:
            lanes.append(f'        <Include href="{prefix}/{file}"/>')

    add(IMAGE_DIR, "image")
    add(SPRITE_DIR, "sprite")
    add(LABEL_DIR, "label")

    lanes.append("    </symbols>")
    return "\n".join(lanes)


# 🔥 reemplazo SEGURO con regex (no rompe nada)
def ReplaceBlock(xml, tag, new):
    patron = rf"<{tag}>.*?</{tag}>"
    return re.sub(patron, new, xml, flags=re.DOTALL)


def main():
    with open(DOM_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    content = ReplaceBlock(content, "media", GenerateMedia())
    content = ReplaceBlock(content, "symbols", GenerateSymbols())

    with open(DOM_FILE, "w", encoding="utf-8") as f:
        f.write(content)

    print("Updated!!")


if __name__ == "__main__":
    main()