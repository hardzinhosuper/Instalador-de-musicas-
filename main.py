# o main.py, (voce vai encontrar no proprio .rar, mas Só Mostrei aqui pra mostrar mesmo!
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
    if len(sys.argv) > 1:
        link = sys.argv[1]
    else:
        link = input("Cole a URL do vídeo do YouTube: ").strip()

    try:
        baixar_mp3(link)
    except Exception as e:
        print(f"\n❌ Ocorreu um erro: {e}")
