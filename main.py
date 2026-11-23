"""Entry program for the 23 November 2026 world-news image bounty.

Copies the front-page image held in this repository to the output path
the harness expects. Deterministic: it copies the same bytes every run
and performs no network access. The copy is verified by comparing file
sizes so a truncated write is never mistaken for a finished entry.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "news.png")
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"

os.makedirs(OUT, exist_ok=True)
dest = os.path.join(OUT, "entry.png")
shutil.copyfile(SRC, dest)
assert os.path.getsize(dest) == os.path.getsize(SRC), "truncated copy"
print("wrote entry.png")
