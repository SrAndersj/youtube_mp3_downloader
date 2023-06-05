# first install  youtube_dl
# but activate enviroment
# source venv/bin/activate
#pip install youtube_dl


import youtube_dl

def descargar_cancion(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == '__main__':
    # URL del video de YouTube
    url = 'https://www.youtube.com/watch?v=vHBjlleWOkk'

    # Llamar a la función para descargar la canción
    descargar_cancion(url)
