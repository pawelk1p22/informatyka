def szyfr_atbash(tekst):
    zaszyfrowany_tekst = ""

    for litera in tekst:
        if litera.isalpha():
            if litera.islower():
                zaszyfrowana_litera = chr(122 - ord(litera) + 97)
            else:
                zaszyfrowana_litera = chr(90 - ord(litera) + 65)
            zaszyfrowany_tekst += zaszyfrowana_litera
        else:
            zaszyfrowany_tekst += litera

    return zaszyfrowany_tekst
