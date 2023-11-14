import mysql.connector
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend

def create_database_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="users"
    )
    return connection

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            encrypted_imie BLOB,
            encrypted_nazwisko BLOB
        )
    """)
    connection.commit()

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = private_key.public_key()

public_key_bytes = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

imie = input("Podaj imię: ")
nazwisko = input("Podaj nazwisko: ")

encrypted_imie = public_key.encrypt(
    imie.encode(),
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

encrypted_nazwisko = public_key.encrypt(
    nazwisko.encode(),
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

connection = create_database_connection()

create_table(connection)

cursor = connection.cursor()
cursor.execute("INSERT INTO users (encrypted_imie, encrypted_nazwisko) VALUES (%s, %s)", (encrypted_imie, encrypted_nazwisko))
connection.commit()

connection.close()

print("Dane dodane do bazy danych.")
