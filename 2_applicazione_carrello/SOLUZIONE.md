# Soluzione

> Implementa una funzione nel modello Product che calcoli e restituisca il prezzo totale di tutti i prodotti presenti in
> una categoria specifica.

Per prima e' stato scritto uno unit test semplice per verificare il corretto funzionamento della funzione
usando `factory_boy` come libreria.

```python
class TestProductManager(TestCase):
    def setUp(self) -> None:
        self.prodotto1 = ProductFactory(category=Categories.FOOD, price=10.00)
        self.prodotto2 = ProductFactory(category=Categories.FOOD, price=15.00)
        self.prodotto2 = ProductFactory(category=Categories.CLOTHES, price=15.00)

    def test_given_product_list_when_get_price_then_return_total_price_by_category(self):
        total_price = Product.objects.get_total_price(category=Categories.FOOD)
        self.assertEqual(total_price, 25.00)
```

Poi e' stato creato un manager per il modello `Product` 

```python
class ProductManager(models.Manager):
    def get_total_price(self, category=None):
        pass
```
che e' stato collegato al model
    
```python
class Product(models.Model):
    ...
    objects = ProductManager()
    ...
```

Infine e' stata implementata la funzione richiesta

```python
class ProductManager(models.Manager):
    def get_total_price(self, category=None):
        return sum([product.price for product in self.filter(category=category)])
```


## Migliorie
E' stata aggiunto il campo al serializer per visualizzare il prezzo totale per la categoria del prodotto

```python
class ProductSerializer(serializers.ModelSerializer):
    total_price = serializers.SerializerMethodField()

    def get_total_price(self, obj):
        return obj.get_total_price(obj.category)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'total_price']
```