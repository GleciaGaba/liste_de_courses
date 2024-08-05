import logging

LOGGER = logging.getLogger()


class Liste(list):
    def __int__(self, nom):
        self.nom = nom

    def ajouter(self, element):
        if not isinstance(element, str):
            raise ValueError("Vous ne pouvez ajouter que des chaînes de caractères !")

        if element in self:
            LOGGER.error(f"{element} est déjà dans la liste.")
            return False

        self.append(element)
        return True

    def afficher(self):


    def enlever(self, element):
        if element in self:
            self.remove(element)
            return True
        return False


if __name__ == '__main__':
    liste = Liste()
    liste.ajouter("Pommes")
    liste.ajouter("Fraises")

    print(liste)




