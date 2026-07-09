#!/usr/bin/env python3
"""MVAS web research helper (stdlib only, no external deps).

Uso:
    python3 scripts/web_research.py "consulta" [n_resultados]

Hace una búsqueda en DuckDuckGo (endpoint HTML), obtiene los N primeros
resultados y extrae el texto legible de cada página. Imprime un digest
condensado (título | url | texto) que el agente usa para investigar e
ingerir en MVAS. No requiere dependencias externas: solo la stdlib.
"""
import sys
import re
import html
import urllib.parse
import urllib.request

DDG = "https://html.duckduckgo.com/html/?q={q}"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"


def _get(url, timeout=15):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    return urllib.request.urlopen(req, timeout=timeout).read()


def search(query, n=5):
    url = DDG.format(q=urllib.parse.quote(query))
    try:
        data = _get(url).decode("utf-8", "ignore")
    except Exception as e:  # noqa: BLE001
        return [], f"search error: {e}"
    # result links: <a class="result__a" href="//duckduckgo.com/l/?uddg=ENCODED">TITLE</a>
    items = re.findall(
        r'class="result__a"[^>]*href="([^"]+)"[^>]*>(.*?)</a>', data, re.S
    )
    results = []
    for href, title in items[:n]:
        m = re.search(r"uddg=([^ \"&]+)", href)
        real = urllib.parse.unquote(m.group(1)) if m else href
        title = re.sub(r"<[^>]+>", "", title)
        results.append((html.unescape(title).strip(), real))
    return results, None


def fetch_text(url, max_chars=2500):
    try:
        data = _get(url)
    except Exception as e:  # noqa: BLE001
        return f"fetch error: {e}"
    if data[:5] == b"%PDF-":
        return "(archivo PDF - citar la URL; usar browser_navigate para leer el texto si se requiere)"
    text = None
    for enc in ("utf-8", "latin-1"):
        try:
            text = data.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    if text is None:
        text = data.decode("utf-8", "ignore")
    text = re.sub(r"<script[\s\S]*?</script>", " ", text, flags=re.I)
    text = re.sub(r"<style[\s\S]*?</style>", " ", text, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) < 40:
        return "(poco texto extraible o bloqueado - citar la URL; usar browser_navigate si se requiere)"
    return text[:max_chars]


def main():
    if len(sys.argv) < 2:
        print('uso: web_research.py "consulta" [n]')
        sys.exit(1)
    query = sys.argv[1]
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    results, err = search(query, n)
    if err:
        print(err)
        sys.exit(0)
    if not results:
        print("sin resultados")
        sys.exit(0)
    print(f"# Resultados para: {query}\n")
    for i, (title, url) in enumerate(results, 1):
        print(f"## {i}. {title}\nURL: {url}\n")
        print(f"TEXTO:\n{fetch_text(url)}\n{'=' * 60}\n")


if __name__ == "__main__":
    main()
