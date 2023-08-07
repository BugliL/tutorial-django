from carrello.models import Cart, Product


class Proxy:
    @classmethod
    def aggiungi_elemento_a_carrello(cls, pk, product_pk):
        # ottengo il carrello dell'utente
        carrello = Cart.objects.get(id=pk)
        # ottengo il prodotto e lo aggiungo al carrello
        prodotto = Product.objects.get(id=product_pk)
        carrello.products.add(prodotto, through_defaults={"quantity": 1})
        return carrello
