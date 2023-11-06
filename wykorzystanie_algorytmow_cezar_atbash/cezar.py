def szyfr_cezara(tekst, przesuniecie):
    zaszyfrowany_tekst = ""

    for litera in tekst:
        if litera.isalpha():
            if litera.islower():
                zaszyfrowana_litera = chr((ord(litera) - ord('a' ) + przesuniecie) % 26 + ord('a'))
            else:
                zaszyfrowana_litera = chr((ord(litera) - ord('A' ) + przesuniecie) % 26 + ord('A'))
            zaszyfrowany_tekst += zaszyfrowana_litera
        else:
            zaszyfrowany_tekst += litera

    return zaszyfrowany_tekst
