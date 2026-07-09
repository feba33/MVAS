#!/usr/bin/env python3
"""Scrape de El Financiero (RSS) -> /tmp/ef_items.txt (top N items).

Usado por el cronjob de ingesta diaria de MVAS. Sin dependencias externas
(solo stdlib). El agente lee /tmp/ef_items.txt y hace el ingest/clasificación.

Uso:  python3 scripts/scrape_elfinanciero.py [N]
"""
import sys
import urllib.request
import xml.etree.ElementTree as ET

RSS = "https://www.elfinanciero.com.mx/arc/outboundfeeds/rss/?outputType=xml"
N = int(sys.argv[1]) if len(sys.argv) > 1 else 8
OUT = "/tmp/ef_items.txt"


def main() -> None:
    req = urllib.request.Request(RSS, headers={"User-Agent": "Mozilla/5.0"})
    data = urllib.request.urlopen(req, timeout=30).read()
    root = ET.fromstring(data)
    items = root.find("channel").findall("item")[:N]
    blocks = []
    for it in items:
        t = (it.findtext("title") or "").strip()
        l = (it.findtext("link") or "").strip()
        p = (it.findtext("pubDate") or "").strip()
        d = (it.findtext("description") or "").strip()
        blocks.append(f"TÍTULO: {t}\nURL: {l}\nFECHA: {p}\nRESUMEN-ORIGINAL: {d}")
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n\n---\n\n".join(blocks))
    print(f"OK {len(items)} items -> {OUT}")


if __name__ == "__main__":
    main()
