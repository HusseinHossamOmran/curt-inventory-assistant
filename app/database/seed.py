from app.database.schema import get_connection, create_tables

PARTS = [
    ("Brake Pads", 12, "Braking", "Mechanical Workshop"),
    ("Brake Discs", 8, "Braking", "Mechanical Workshop"),
    ("ECU", 2, "Electrical", "Electronics Lab"),
    ("Wiring Harness", 5, "Electrical", "Electronics Lab"),
    ("Suspension Spring", 6, "Suspension", "Mechanical Workshop"),
    ("Shock Absorber", 4, "Suspension", "Mechanical Workshop"),
    ("Steering Wheel", 1, "Steering", "Cockpit Storage"),
    ("Radiator", 2, "Cooling", "Engine Bay Storage"),
    ("Fuel Pump", 3, "Fuel System", "Engine Bay Storage"),
    ("Battery", 2, "Electrical", "Electronics Lab"),
    ("Tires (Slick)", 8, "Wheels", "Garage Storage"),
    ("Carbon Fiber Sheet", 10, "Chassis", "Fabrication Room"),
]

def seed_parts():
    create_tables()
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM parts")
    count = cursor.fetchone()[0]

    if count > 0:
        print(f"Parts table already has {count} rows. Skipping seed.")
        conn.close()
        return

    cursor.executemany(
        "INSERT INTO parts (name, quantity, category, location) VALUES (?, ?, ?, ?)",
        PARTS
    )
    conn.commit()
    conn.close()
    print(f"Seeded {len(PARTS)} parts.")

if __name__ == "__main__":
    seed_parts()