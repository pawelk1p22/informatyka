import mysql.connector

def szyfruj_cezar(imie, przesuniecie):
    zaszyfrowane_imie = ""
    for litera in imie:
        if litera.isalpha():
            if litera.isupper():
                kod_litery = ord('A')
            else:
                kod_litery = ord('a')
            zaszyfrowana_litera = chr((ord(litera) - kod_litery + przesuniecie) % 26 + kod_litery)
            zaszyfrowane_imie += zaszyfrowana_litera
        else:
            zaszyfrowane_imie += litera
    return zaszyfrowane_imie

def szyfruj_atbash(nazwisko):
    zaszyfrowane_nazwisko = ""
    for litera in nazwisko:
        if litera.isalpha():
            if litera.isupper():
                kod_litery = ord('A')
            else:
                kod_litery = ord('a')
            zaszyfrowana_litera = chr(25 - (ord(litera) - kod_litery) + kod_litery)
            zaszyfrowane_nazwisko += zaszyfrowana_litera
        else:
            zaszyfrowane_nazwisko += litera
    return zaszyfrowane_nazwisko

def deszyfruj_cezar(imie, przesuniecie):
    return szyfruj_cezar(imie, -przesuniecie)

def deszyfruj_atbash(nazwisko):
    return szyfruj_atbash(nazwisko) 

def dodaj_do_bazy_danych(imie, nazwisko):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='users'
    )

    cursor = conn.cursor()

    imie_zaszyfrowane = szyfruj_cezar(imie, 3)

    nazwisko_zaszyfrowane = szyfruj_atbash(nazwisko)

    sql = "INSERT INTO users (imie, nazwisko) VALUES (%s, %s)"
    values = (imie_zaszyfrowane, nazwisko_zaszyfrowane)

    cursor.execute(sql, values)
    conn.commit()

    cursor.close()
    conn.close()


def wyswietl_rekordy():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='users'
    )
    cursor = conn.cursor()
    sql = "SELECT imie, nazwisko FROM users"
    cursor.execute(sql)
    for (imie, nazwisko) in cursor:
        odszyfrowane_imie = deszyfruj_cezar(imie, 3)
        odszyfrowane_nazwisko = deszyfruj_atbash(nazwisko)
        print(f"\033[95mImię \033[94m(zaszyfrowane)\033[0m: \033[92m{imie}\033[0m, \033[95mImię \033[94m(odszyfrowane)\033[0m: \033[0m\033[91m{odszyfrowane_imie}\033[0m")
        print(f"\033[95mNazwisko \033[94m(zaszyfrowane)\033[0m: \033[92m{nazwisko}\033[0m, \033[95mNazwisko \033[94m(odszyfrowane)\033[0m: \033[0m\033[91m{odszyfrowane_nazwisko}\033[0m")
        print(f"\033[93m--------------------------------------------\033[0m")

        print
    cursor.close()
    conn.close()

def dodaj_do_bazy_danych(imie, nazwisko):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='users'
    )

    cursor = conn.cursor()

    imie_zaszyfrowane = szyfruj_cezar(imie, 3)

    nazwisko_zaszyfrowane = szyfruj_atbash(nazwisko)

    sql = "INSERT INTO users (imie, nazwisko) VALUES (%s, %s)"
    values = (imie_zaszyfrowane, nazwisko_zaszyfrowane)

    cursor.execute(sql, values)
    conn.commit()

    cursor.close()
    conn.close()


def menu():
    print(f"\033[97m1. Dodaj rekord")
    print("2. Wyświetl rekordy")
    print("3. Wyjdź\033[0m")

def main():
    while True:
        menu()
        choice = input("Wybierz opcję: ")

        if choice == "1":
            imie = input("Podaj imię: ")
            nazwisko = input("Podaj nazwisko: ")
            dodaj_do_bazy_danych(imie, nazwisko)
        elif choice == "2":
            wyswietl_rekordy()
        elif choice == "3":
            break
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")

    
main()
