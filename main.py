"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Jakub Šmíd
email: smidjakub13@gmail.com
"""

from random import sample, randint


def vygeneruje_zadani(pocet_cislic) -> list:
    """generuje hádaný kód o daném počtu unikátních znaků (max 10)"""

    zadani = []
    prvni_z_cisel = randint(1,9)
    zbyle_cislice = [x for x in range(0, 10) if x != prvni_z_cisel]
    dalsi_cisla = sample(zbyle_cislice,pocet_cislic-1)
    zadani.append(prvni_z_cisel)
    zadani.extend(dalsi_cisla)

    return (zadani)


def vyzada_cisla_uzivatele(pocet_cislic) -> list:
    """ošetřuje zadání od uživatele - vyžaduje daný počet unikátních číselných znaků"""

    while True:
        zadane_cislo = input(">>> ")
        if zadane_cislo.isdigit() and len(zadane_cislo) == pocet_cislic == len(
            set(zadane_cislo)
        ):
            zpracovane_zadane_cislo = [int(i) for i in zadane_cislo]
            """alternativa, pokud chceme uživateli zakázat jako první znak nulu. 
            Vlastně si nejsem jistej, jaký má ta hra pravidla 
            a proč tu nulu na začátku omezujeme."""
            #if int(zadane_cislo) < 1000:
            #    print("The first digit cannot be zero.")
            #else:
            #    break
            break
        else:
            print(f"It must be {pocet_cislic} unique digits.")
    return zpracovane_zadane_cislo


def kontrola_bulls_and_cows(
    cisla_od_uzivatele: list, 
    cisla_od_pocitace: list, 
    pocet_cislic: int
) -> dict:
    
    """Zapisuje shody úplné i částečné"""
    dobytek = {"cow": 0, "bull": 0}
    for i in range(pocet_cislic):
        if cisla_od_uzivatele[i] == cisla_od_pocitace[i]:
            dobytek["bull"] += 1
        elif cisla_od_uzivatele[i] in cisla_od_pocitace:
            dobytek["cow"] += 1

    return dobytek


def sumarizace_vysledku(dobytek: dict) -> bool:
    """Zpracuje výstup z kontrola_bulls_and_cows a vypíše vysledek, 
    nebo iniciuje pogratulování."""

    if dobytek["bull"] == 4:
        print(oddelovac)
        return True

    else:
        bull_s = "bulls" if dobytek["bull"] != 1 else "bull"
        cow_s = "cows" if dobytek["cow"] != 1 else "cow"
        print(
            f"{dobytek['bull']} {bull_s}, " f"{dobytek['cow']} {cow_s}\n" f"{oddelovac}"
        )
        return False

# neměnné start
oddelovac = 47 * "-"
vytezstvi = False
pocet_kol = 0
# neměnné konec

pocet_cislic = 4 # proměnná určující počet číslic v zadání. Max 10.


print(
    f"Hi there!\n{oddelovac}\n"
    "I've generated a random 4 digit number for you.\n"
    f"Let's play a bulls and cows game.\n{oddelovac}"
)

cisla_pocitace = vygeneruje_zadani(pocet_cislic)

print(f"Enter {pocet_cislic} numbers:")

while not vytezstvi:
    """ústřední část"""

    pocet_kol += 1  # započítá započaté kolo
    cisla_uzivatele = vyzada_cisla_uzivatele(pocet_cislic)
    porovnani = kontrola_bulls_and_cows(cisla_uzivatele, cisla_pocitace, pocet_cislic)

    vytezstvi = sumarizace_vysledku(porovnani)
print(
    f"""Correct, you've guessed the right number in {pocet_kol} guesses!
{oddelovac}\nThat's amazing"""
)
