from app.database.schema import get_connection

def get_part(name: str):
    """Exact or partial match on part name (case-insensitive)."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM parts WHERE LOWER(name) LIKE LOWER(?)",
        (f"%{name}%",)
    )
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

def get_by_category(category: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM parts WHERE LOWER(category) LIKE LOWER(?)",
        (f"%{category}%",)
    )
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def update_quantity(name: str, delta: int):
    """Adjust quantity by delta (can be negative). Returns updated row or None."""
    part = get_part(name)
    if not part:
        return None

    conn = get_connection()
    cursor = conn.cursor()
    new_quantity = max(0, part["quantity"] + delta)
    cursor.execute(
        "UPDATE parts SET quantity = ? WHERE id = ?",
        (new_quantity, part["id"])
    )
    conn.commit()
    conn.close()
    return get_part(name)

def get_all_parts():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM parts")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]