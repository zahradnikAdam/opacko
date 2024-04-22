cisla = [3, 5, 8, 1, 2, 4, 6, 7]
 
def seradit_cisla(cisla, sestupne=False):
    serazena_cisla = sorted(cisla, reverse=sestupne)
    return serazena_cisla
 
def vyber_poradi():
    volba = input("Chceš čísla seřadit vzestupně (A) nebo sestupně (B)? ").upper()
    return volba == 'B'
 
sestupne = vyber_poradi()
print("Čísla seřazená:", seradit_cisla(cisla, sestupne))