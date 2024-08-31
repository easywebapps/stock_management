
class Categorie:

    def __init__(self, name: str):
        self.__name= name
    def __call__(self):
        return self.__name

class Marque:
    
    def __init__(self, name: str):
        self.__name= name
    def __call__(self):
        return self.__name

class Produit:

    def __init__(self, reference: str, categorie: str, marque: str, description, prix_achat, gain)