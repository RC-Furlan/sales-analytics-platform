from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

SQL_DIR = BASE_DIR / "sql" / "business"
print(SQL_DIR)


def load_sql(filename: str) -> str:
    """
    Load a SQL file from sql/business.
    """

    file_path = SQL_DIR / filename

    with open(file_path, encoding="utf-8") as file:
        return file.read()