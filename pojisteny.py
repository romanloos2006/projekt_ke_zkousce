class Pojisteny:
    """
    Třída reprezentuje pojištěného
    """

    def __init__(self, jmeno, prijmeni, vek, telefon):
        """
        Konstruktor nového pojištěného
        jmeno: jméno
        prijmeni: příjmení
        vek: věk
        telefon: telefonní číslo
        """
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        """
        Vrací textovou reprezentaci pojištěného
        """
        return f"{self.jmeno} {self.prijmeni} {self.vek} {self.telefon}"
