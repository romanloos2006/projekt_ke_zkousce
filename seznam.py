from pojisteny import Pojisteny


class Seznam:

    """
    Třída reprezentuje seznam pojištěných
    """

    def __init__(self):
        """
        Vytvoří nový seznam pojištěných
        seznam_pojistenych: seznam pojištěných
        """
        self.seznam_pojistenych = []

    def pridat_pojisteneho(self):
        """
        Přidá nového pojištěného do seznamu pojištěných
        """
        jmeno = input("Zadejte jméno pojištěného:\n")
        prijmeni = input("Zadejte příjmení pojištěného:\n")
        vek = input("Zadejte věk pojištěného:\n")
        telefon = input("Zadejte telefonní číslo pojištěného:\n")
        novy_pojisteny = Pojisteny(jmeno, prijmeni, vek, telefon)
        self.seznam_pojistenych.append(novy_pojisteny)

    def vypsat_pojistene(self):
        """
        Vypíše všechny pojištěné v seznamu pojištěných
        """
        for pojisteny in self.seznam_pojistenych:
            print(pojisteny)

    def vyhledat_pojisteneho(self):
        """
        Vyhledá a vypíše pojištěného v seznamu pojištěných
        """
        jmeno = input("Zadejte jméno pojištěného:\n")
        prijmeni = input("Zadejte příjmení pojištěného:\n")
        for pojisteny in self.seznam_pojistenych:
            if jmeno == pojisteny.jmeno:
                if prijmeni == pojisteny.prijmeni:
                    print(pojisteny)
                else:
                    print("Tato osoba není v seznamu pojištěných.")
