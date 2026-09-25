import sqlite3
from pathlib import Path


# ============================================================
# DATABASE PATH
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = BASE_DIR / "database" / "skillcompass.db"


# ============================================================
# CONNECT
# ============================================================

connection = sqlite3.connect(DB_PATH)

cursor = connection.cursor()


# ============================================================
# CHECK EXISTING COLUMNS
# ============================================================

cursor.execute("PRAGMA table_info(users)")

existing_columns = {
    row[1]
    for row in cursor.fetchall()
}


print("Existing columns:")
print(existing_columns)


# ============================================================
# ADD AGE
# ============================================================

if "age" not in existing_columns:

    cursor.execute(
        "ALTER TABLE users ADD COLUMN age INTEGER"
    )

    print("Added column: age")

else:

    print("Column already exists: age")


# ============================================================
# ADD DATE OF BIRTH
# ============================================================

if "date_of_birth" not in existing_columns:

    cursor.execute(
        "ALTER TABLE users ADD COLUMN date_of_birth TEXT"
    )

    print("Added column: date_of_birth")

else:

    print("Column already exists: date_of_birth")


# ============================================================
# ADD STAGE
# ============================================================

if "stage" not in existing_columns:

    cursor.execute(
        "ALTER TABLE users ADD COLUMN stage TEXT"
    )

    print("Added column: stage")

else:

    print("Column already exists: stage")


# ============================================================
# SAVE CHANGES
# ============================================================

connection.commit()


# ============================================================
# VERIFY
# ============================================================

cursor.execute("PRAGMA table_info(users)")

columns = cursor.fetchall()

print("\nUpdated users table:")

for column in columns:
    print(
        f"{column[1]} | "
        f"{column[2]} | "
        f"nullable={not column[3]}"
    )


# ============================================================
# CLOSE
# ============================================================

connection.close()

print("\nDatabase migration completed successfully.")