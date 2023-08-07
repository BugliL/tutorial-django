from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase

from carrello.models import Product, Cart


class CarrelloTest(APITestCase):
    def setUp(self):
        # Creare un utente di test
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')
        self.product, _ = Product.objects.get_or_create(name="testproduct", price=10.0, description="testdescription")
        self.cart, _ = Cart.objects.get_or_create(user=self.user)

    def test_crea_carrello(self):
        # Verifica che il carrello venga creato correttamente

        # Assicurati che tu stia usando l'URL corretto per l'endpoint di creazione del carrello
        # usando il reverse dell'url
        url = reverse('carts-list')

        # Creazione dei dati per la richiesta POST
        data = {
            'user_id': self.user.id,
            'products': [
                {'name': 'Prodotto 2', 'description': 'Descrizione prodotto 2', 'price': 19.99}
            ]
        }
        # Esegui la richiesta POST per creare il carrello
        response = self.client.post(url, data, format='json')

        # Controlla che la risposta abbia un codice di stato 201 (CREATED) che indica il successo della creazione del carrello
        self.assertEqual(response.status_code, 201, msg=response.data)
        self.assertEqual(response.data['user']['username'], self.user.username, msg=response.data)
        self.assertEqual(len(response.data['products']), 1, msg=response.data)

        product = response.data['products'].pop()
        self.assertEqual(product['name'], 'Prodotto 2', msg=response.data)

    def test_aggiungi_prodotto(self):
        url = reverse('carts-aggiungi-prodotto', kwargs={'pk': self.cart.id, 'product_pk': self.product.id})
        response = self.client.post(url)

        # Verifica che la risposta abbia status code 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verifica che il prodotto sia stato aggiunto correttamente al carrello
        self.cart.refresh_from_db()
        self.assertIn(self.product, self.cart.products.all())
