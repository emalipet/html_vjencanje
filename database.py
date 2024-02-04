import sqlite3


def create_tables():
    connection = sqlite3.connect('guests.db')
    cursor = connection.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS guests (id INTEGER PRIMARY KEY, name TEXT, companion_name TEXT, child_name TEXT)')
    connection.commit()
    connection.close()


create_tables()


def add_guest(guest_name, companion_name=None, child_name=None):
    connection = sqlite3.connect('guests.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO guests (name, companion_name, child_name) VALUES (?, ?, ?)',
                   (guest_name, companion_name, child_name))
    connection.commit()
    connection.close()


def read_guests():
    connection = sqlite3.connect('guests.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM guests')
    guests = cursor.fetchall()
    connection.close()
    return guests


# Pozivamo funkciju za čitanje gostiju
guests = read_guests()

# Ispisujemo sve goste
for guest in guests:
    print(guest)
