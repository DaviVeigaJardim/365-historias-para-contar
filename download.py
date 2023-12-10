import tempfile

import httplib2


def download_stories(date: str = "maio4"):
    h = httplib2.Http(".cache")
    (_, content) = h.request(method='GET',
                             uri=f'https://www.multygraf.com.br/pedaletra/365historias/conteudo/{date}.mp3')

    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(content)
        f.close()

        return f.name
