import sqlite3
import hashlib

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
               username TEXT,
               password_hash TEXT
)
""")

conn.commit()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register(username, password):
    pw_hash = hash_password(password)

    try:
        cursor.execute(
            "INSERT INTO users (username, password_hash) VALUES (?, ?)",
            (username, pw_hash)
        )
        conn.commit()
        print("Register berhasil")
    except sqlite3.IntegrityError:
        print("Username sudah dipakai")

def login(username, password):
    cursor.execute(
        "SELECT password_hash FROM users WHERE username = ?",
        (username,)
    )

    result = cursor.fetchone()

    if not result:
        print("User tidak ditemukan")
        return
    
    stored_hash = result[0]
    input_hash = hash_password(password)

    if input_hash == stored_hash:
        print("Login berhasil")
        print(password)
    else:
        print("Password salah")
        print(password)

while True:
    print("\n=== SIMPLE LOGIN SYSTEM ===")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Pilih: ")

    if choice == "1":
        u = input("Masukkan Username: ")
        p = input("Masukkan Password: ")
        register(u, p)

    elif choice == "2":
        u = input("Masukkan Username: ")
        p = input("Masukkan Password: ")
        login(u, p)

    elif choice == "3":
        break

    else:
        break