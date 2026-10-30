#!/usr/bin/env python3
"""Baixa as mídias geradas no Higgsfield para a pasta assets/.

Roda sozinho no GitHub Actions (veja .github/workflows/midias.yml).
A lista de arquivos e links fica em assets/midias.json.
Imagens são convertidas para WebP; o vídeo é recomprimido, sem áudio.
Arquivos que já existem em assets/ não são baixados de novo.
"""
import io
import json
import os
import shutil
import subprocess
import urllib.request

from PIL import Image

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(RAIZ, "assets")


def baixar(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (site-luciane-almeida)"})
    with urllib.request.urlopen(req, timeout=180) as resp:
        return resp.read()


def salvar_imagem(dados, destino, largura):
    im = Image.open(io.BytesIO(dados)).convert("RGB")
    if im.width > largura:
        im = im.resize((largura, round(im.height * largura / im.width)), Image.LANCZOS)
    im.save(destino, "WEBP", quality=80, method=6)


def salvar_video(dados, destino):
    if not shutil.which("ffmpeg"):
        with open(destino, "wb") as f:
            f.write(dados)
        return
    bruto = destino + ".orig.mp4"
    with open(bruto, "wb") as f:
        f.write(dados)
    subprocess.run(
        ["ffmpeg", "-loglevel", "error", "-y", "-i", bruto, "-an",
         "-c:v", "libx264", "-preset", "veryfast", "-crf", "26",
         "-pix_fmt", "yuv420p", "-movflags", "+faststart", destino],
        check=True,
    )
    os.remove(bruto)


def main():
    with open(os.path.join(ASSETS, "midias.json"), encoding="utf-8") as f:
        itens = json.load(f)
    for item in itens:
        destino = os.path.join(ASSETS, item["arquivo"])
        if os.path.exists(destino) and os.path.getsize(destino) > 0:
            print("já existe:", item["arquivo"])
            continue
        dados = baixar(item["url"])
        if destino.endswith(".webp"):
            salvar_imagem(dados, destino, item.get("largura", 1100))
        elif destino.endswith(".mp4"):
            salvar_video(dados, destino)
        else:
            with open(destino, "wb") as f:
                f.write(dados)
        print("baixado:", item["arquivo"], os.path.getsize(destino) // 1024, "KB")


if __name__ == "__main__":
    main()
