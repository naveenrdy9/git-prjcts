import sqlite3

def create_tables():
    try:
        conn = sqlite3.connect('fms.db')
        cursor = conn.cursor()

        # Create admin table
        cursor.execute('''CREATE TABLE IF NOT EXISTS admin (
                            user_name VARCHAR(50) NOT NULL,
                            password VARCHAR(50) NOT NULL,
                            email VARCHAR(50),
                            PRIMARY KEY(user_name)
                        )''')

        # Create donation_details table
        cursor.execute('''CREATE TABLE IF NOT EXISTS donation_details (
                            donation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            item_no INTEGER,
                            item_name TEXT,
                            item_type TEXT,
                            calories INTEGER,
                            amount_lb INTEGER,
                            servings INTEGER,
                            manager_id INTEGER,
                            donation_status TEXT DEFAULT 'pending',
                            user_id INTEGER,
                            FOREIGN KEY(manager_id) REFERENCES managers(manager_id)
                        )''')

        # Create managers table
        cursor.execute('''CREATE TABLE IF NOT EXISTS managers (
                            manager_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            first_name VARCHAR(50),
                            last_name VARCHAR(50),
                            user_name VARCHAR(50) NOT NULL,
                            password VARCHAR(50) NOT NULL,
                            department VARCHAR(50),
                            email VARCHAR(50)
                        )''')

        # Create users table
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            first_name VARCHAR(50) NOT NULL,
                            last_name VARCHAR(50) NOT NULL,
                            user_name VARCHAR(50) NOT NULL,
                            password VARCHAR(50) NOT NULL,
                            email VARCHAR(50),
                            mobile_no VARCHAR(50) NOT NULL
                        )''')

        conn.commit()
        print("Tables created successfully.")

    except sqlite3.Error as e:
        print("Error creating tables:", e)

    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    create_tables()
