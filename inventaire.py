from pysondb import db

class Produit:

    def __init__(self, reference: str, categorie: str, marque: str, description: str, prix_achat: int, gain: float= .25, **kwargs):
        
        self.reference= reference
        self. categorie= categorie
        self.marque= marque
        self.description= description
        self.prix_achat= prix_achat
        self.gain= gain if 'prix_vente' not in kwargs else round(kwargs['prix_vente'] / prix_achat, 2)
        self.prix_vente= kwargs['prix_vente'] if 'prix_vente' in kwargs else round (prix_achat * (1+gain))


class Inventaire:

    def __init__(self):
        self.bd_produits= db.getDb("produits.json")
        self.produits= self.bd_produits.getAll()
        self.marques= self.__load_marques()
        self.categories= self.__load_categories()


    def __load_marques(self):
        with open('marques.txt', 'r', encoding='utf-8') as f:
            marques= f.read().split('\n')
        return marques
    
    def __load_categories(self):
        with open('categories.txt', 'r', encoding='utf-8') as f:
            categories= f.read().split('\n')
        return categories
    
    def ajouter_marque(self, marque: str) -> None:
        if marque not in self.marques:
            with open('marques.txt', 'a', encoding='utf-8') as f:
                f.write(f'{marque}\n')
    
    def ajouter_categorie(self, categorie: str) -> None:
        if categorie not in self.categories:
            with open('categories.txt', 'a', encoding='utf-8') as f:
                f.write(f'{categorie}\n')

    
    def ajouter_produit(self, reference: str, categorie: str, marque: str, description: str, prix_achat: int, gain: float= .25, quantite: int= 1, **kwargs):

        
        produit= Produit(reference, categorie, marque, description, prix_achat, gain, **kwargs)
        produit= produit.__dict__
        produit.update({'quantite': quantite})       

        self.bd_produits.add(produit)
