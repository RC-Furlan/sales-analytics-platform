from pathlib import Path


def load_sql(filename: str) -> str:

    project_root = Path(__file__).resolve().parent

    sql_file = project_root / "sql" / "business" / filename

    with open(sql_file, "r", encoding="utf-8") as f:
        return f.read()