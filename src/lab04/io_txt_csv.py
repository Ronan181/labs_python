from pathlib import*
import csv
from typing import Iterable, Sequence
import sys
import os

sys.path.append('/Users/ars/Documents/GitHub/labs_python/src/lib/')
from text import *

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError
    try:
        text=path.read_text(encoding=encoding)
        text=normalize(text)
        return text
    except UnicodeDecodeError as a:
        raise UnicodeDecodeError() from a

def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    if rows:
        for row in rows:
            if len(row)!=len(rows[0]):
                raise ValueError
    if header and rows and len(header)!=len(rows[0]):
        raise ValueError
    p = Path(path)
    rows = list(rows)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)
            
write_csv([("word","count"),("test",3)], "data/check.csv")  
txt = read_text("data/input.txt") 
print(txt)
