from seznam import Seznam

seznam_pojistenych = Seznam()


def nove_zadani():
    nezadano = True
    while nezadano:
        odpoved = input("\nPřejete si pokračovat? y / n: ")
        if odpoved == "y" or odpoved == "Y":
            return True
        elif odpoved == "n" or odpoved == "N":
            return False
        else:
            pass


def volba():
    pokracovat = "ano"
    while pokracovat == "ano":
        print("1 - Přidat nového pojištěného")
        print("2 - Vypsat všechny pojištěné")
        print("3 - Vyhledat pojištěného")
        print("4 - Konec")
        cislo_operace = input("Zadejte číslo (1 - 4):\n")
        if cislo_operace == "1":
            seznam_pojistenych.pridat_pojisteneho()
            print("Data byla uložena.")
            break
        elif cislo_operace == "2":
            seznam_pojistenych.vypsat_pojistene()  # Zavolá funkci pro vypsání všech pojištěných
            break
        elif cislo_operace == "3":
            seznam_pojistenych.vyhledat_pojisteneho()  # Zavolá funkci pro vyhledání pojištěného
            break
        elif cislo_operace == "4":
            break
        else:
            print("Neplatná volba!")


def main():
    print("----------------------")
    print("Evidence pojištěných")
    print("----------------------")
    pokracovat = True
    while pokracovat:
        volba()
        if nove_zadani():
            pass
        else:
            pokracovat = False
    input("\nStiskněte klávesu Enter...")


main()
