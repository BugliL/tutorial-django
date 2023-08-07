# Applicazione carrello

In questo progetto vengono presentate le principali caratteristiche di drf e la struttura di base di una applicazione.

## Creazione dell'applicazione

Il senso delle applicazioni di Django è organizzare il codice in modo modulare e separato per affrontare diversi compiti
o funzionalità all'interno di un progetto. Ogni applicazione in Django ha uno scopo specifico e può essere sviluppata,
testata e mantenuta in modo indipendente dal resto del progetto.

Per creare questo progetto, dopo aver installato le dipendenze e' stato lanciato il comando:

```shell
python manage.py startapp carrello
```

Questo comando crea una cartella con il nome dell'applicazione con dentro tutti i file necessari per il suo
funzionamento.
Per utilizzare il `Django Rest Framework` e' necessario aggiungere un paio di file alla cartella come notazione:

- `serializers.py`: file che contiene i serializer dell'applicazione
- `urls.py`: file che contiene le url dell'applicazione

## Struttura file dell'applicazione

```
negozio
├── negozio
└── carrello
    ├── migrations
    │   └── __init__.py
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── serializers.py
    ├── tests.py
    ├── urls.py
    └── views.py
```

- `migrations`: cartella che contiene i file di migrazione del database
- `__init__.py`: file che indica che la cartella e' un package
- `admin.py`: file che contiene la configurazione dell'interfaccia di amministrazione
- `apps.py`: file che contiene la configurazione dell'applicazione
- `models.py`: file che contiene i modelli dell'applicazione
- `serializers.py`: file che contiene i serializer dell'applicazione
- `tests.py`: file che contiene i test dell'applicazione
- `views.py`: file che contiene le view dell'applicazione

## Migrazioni

Le migrazioni sono file che contengono le istruzioni per creare o modificare le tabelle del database. Questi file sono
generati automaticamente da Django quando si creano o si modificano i modelli. Per creare le migrazioni bisogna lanciare
il comando:

```shell
python manage.py makemigrations
```

il risultato di questo comando e' la creazione di un file nella cartella `migrations` con il nome `0001_initial.py` che
contiene le istruzioni per creare le tabelle del database.

Per applicare le migrazioni bisogna lanciare il comando:

```shell
python manage.py migrate
```

per tornare indietro di una migrazione bisogna lanciare il comando:

```shell
python manage.py migrate carrello 0001
```

dove viene specificato il nome dell'applicazione ed il numero della migrazione a cui si vuole tornare indietro.
Nel caso si volessero annuallare tutte le migrazioni di una applicazione e ricrearle da capo bisogna lanciare il
comando:

```shell
python manage.py migrate carrello zero
```

Altri comandi utili per le migrazioni sono:

- `showmigrations`: mostra lo stato delle migrazioni
- `sqlmigrate`: mostra il codice sql di una migrazione
- `migrate --fake`: applica una migrazione senza eseguire il codice sql
- `migrate --fake-initial`: applica la migrazione iniziale senza eseguire il codice sql
- `migrate --list`: mostra tutte le migrazioni eseguite e non eseguite
- `migrate --plan`: mostra le migrazioni che verranno eseguite
- `migrate --run-syncdb`: crea le tabelle per le applicazioni che non hanno migrazioni

Applicate le migrazioni e' possibile vedere le tabelle create nel database e facendo il run dell'applicazione e'
possibile
consultare l'interfaccia swagger per vedere le api create.

## Serializer

Il loro obiettivo e' quello di fornire un modo semplice per serializzare e deserializzare i dati. Si collegano ai
modelli e trasformano i dati in un formato che puo' essere facilmente consumato da un client.

## ViewSet

I ViewSet sono una classe che raggruppa le view che forniscono le operazioni CRUD per un modello. I ViewSet sono
implementati come classi che estendono la classe `GenericViewSet` e forniscono i metodi per le operazioni CRUD.

## Admin

L'interfaccia di amministrazione e' un'interfaccia web che permette di gestire i dati del database.
In questo esempio e' stata configurata per gestire i dati del modello `Carrello` e `Prodotto` usando
un `InlineModelAdmin`: un modello che viene gestito all'interno dell'interfaccia di un altro modello in modo da non
doversi spostare da una interfaccia all'altra.