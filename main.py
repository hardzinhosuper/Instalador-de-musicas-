"""
Script para baixar áudio de vídeos do YouTube e converter para MP3.

Requisitos:
    pip install yt-dlp
    ffmpeg instalado no sistema (necessário para a conversão para MP3)

Uso:
    python baixar_mp3.py
    (depois é só colar a URL quando for solicitado)

Ou direto pela linha de comando:
    python baixar_mp3.py "https://www.youtube.com/watch?v=XXXXXXXX"
"""

import sys
import os
from yt_dlp import YoutubeDL


def baixar_mp3(url: str, pasta_destino: str = "downloads"):
    """
    Baixa o áudio de um vídeo (ou playlist) do YouTube e salva como MP3.

    Args:
        url: URL do vídeo ou playlist do YouTube.
        pasta_destino: pasta onde os arquivos MP3 serão salvos.
    """
    os.makedirs(pasta_destino, exist_ok=True)

    opcoes = {
        # Pega o melhor formato de áudio disponível
        "format": "bestaudio/best",
        # Template do nome do arquivo de saída
        "outtmpl": os.path.join(pasta_destino, "%(title)s.%(ext)s"),
        # Pós-processamento: extrai o áudio e converte para MP3
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",  # qualidade em kbps
            }
        ],
        "noplaylist": True,  # mude para False se quiser baixar playlists inteiras
        "quiet": False,
    }

    with YoutubeDL(opcoes) as ydl:
        print(f"Baixando: {url}")
        ydl.download([url])
        print(f"\n✅ Concluído! Arquivo(s) salvo(s) em: {os.path.abspath(pasta_destino)}")


if __name__ == "__main__":
    print("=" * 50)
    print("  Baixador de Músicas do YouTube (MP3)")
    print("=" * 50)
    print("Digite 'sair' a qualquer momento para fechar o programa.\n")

    # Se o usuário passar uma URL direto pela linha de comando,
    # baixa ela primeiro antes de entrar no loop
    if len(sys.argv) > 1:
        primeiro_link = sys.argv[1]
        try:
            baixar_mp3(primeiro_link)
        except Exception as e:
            print(f"\n❌ Ocorreu um erro: {e}")

    while True:
        link = input("\nCole a URL do vídeo do YouTube: ").strip()

        if link.lower() in ("sair", "exit", "quit", ""):
            print("Encerrando... até a próxima! 🎧")
            break

        try:
            baixar_mp3(link)
        except Exception as e:
            print(f"\n❌ Ocorreu um erro: {e}")
            print("Tente novamente com outra URL ou digite 'sair' para encerrar.")
