import pytest
import json
import csv
import sys
from pathlib import Path

sys.path.append("/Users/ars/Documents/GitHub/labs_python/src/lab05/")
from json_csv import *
from csv_xlsx import *

# Позитивные сценарии


def test_json_to_csv_positive(tmp_path: Path):
    src = tmp_path / "input.json"
    dst = tmp_path / "output.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(src), str(dst))
    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 2
    assert set(rows[0].keys()) == {"name", "age"}
    assert rows[0]["name"] == "Alice"


def test_csv_to_json_positive(tmp_path: Path):
    src = tmp_path / "input.csv"
    dst = tmp_path / "output.json"
    with src.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerow({"name": "Alice", "age": "22"})
        writer.writerow({"name": "Bob", "age": "25"})
    csv_to_json(str(src), str(dst))
    result = json.loads(dst.read_text(encoding="utf-8"))
    assert len(result) == 2
    assert set(result[0].keys()) == {"name", "age"}
    assert result[1]["name"] == "Bob"


# Негативные сценарии


@pytest.mark.parametrize(
    "case",
    [
        (json_to_csv, "json", "", ValueError),
        (csv_to_json, "csv", "", ValueError),
        (json_to_csv, "json", None, FileNotFoundError),
        (csv_to_json, "csv", None, FileNotFoundError),
    ]
)
def test_negative_cases(tmp_path: Path, case):
    converter, ext, content, exc = case
    src = tmp_path / f"bad.{ext}"
    dst = tmp_path / "out.tmp"
    if content is not None:
        src.write_text(content, encoding="utf-8")
    with pytest.raises(exc):
        converter(str(src), str(dst))
