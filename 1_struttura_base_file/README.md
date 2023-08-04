# Progetto negozio
In questo progetto vengono presentate le principali funzionalità di Django e la struttura di base.

## Creazione del progetto
Per creare questo progetto, dopo aver installato le dipendenze e' stato lanciato il comando:
```shell
django-admin startproject negozio
```
Questo comando crea una cartella con il nome del progetto e al suo interno una cartella con lo stesso nome e un
file `manage.py` che serve per gestire il progetto.

## Struttura base delle cartelle del progetto `negozio`
```
negozio
├── negozio
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```
- `negozio`: cartella che contiene i file principali del progetto, serve per raggruppare i file da lanciare col server
- `__init__.py`: file che indica che la cartella e' un package
- `asgi.py`: file di configurazione per il protocollo Asynchronous Server Gateway Interface (ASGI), serve per avviare l'applicazione
- `wsgi.py`: file di configurazione per il protocollo Web Server Gateway Interface (WSGI), serve per avviare l'applicazione
- `settings.py`: file di configurazione del progetto contenente le impostazioni principali
- `urls.py`: file che contiene le rotte dell'applicazione e le associazioni con le view del progetto

`asgi.py` e `wsgi.py` sono file di configurazione per il protocollo di comunicazione tra il server e l'applicazione,
sono i file utilizzati da `Gunicorn` per avviare l'applicazione.

Il progetto e' gia' funzionante senza definire nessuna applicazione aggiuntiva e per avviarlo basta lanciare il comando: 
```shell
python manage.py runserver 0.0.0.0:8001
```
Questo comando avvia il server di sviluppo di Django, e' pensato per essere utilizzato solo in fase di sviluppo, per la
produzione e' OBBLIGO utilizzare una configurazione con un server web fatto apposta.

## Schema di configurazione di produzione 
Qui riporto lo schema di funzionamento di un server web con l'utilizzo di Gunicorn, Nginx e Django senza entrare nei
dettagli di configurazione.
```
        +-------+            +----------+            +--------+
        | Nginx | ---------> | Gunicorn | ---------> | Django |
        +-------+            +----------+            +--------+
```
Ogni componente ha un ruolo ben preciso e serve per dare massima flessibilità al progetto.  
`Nginx` ha il ruolo di proxy. Nasconde la configurazione specifica dell'applicazione e protegge il server Gunicorn, che
esegue il codice Django, dall'accesso diretto. Inoltre, Nginx può essere configurato per gestire aspetti di sicurezza
come SSL/TLS, garantendo una comunicazione crittografata tra client e server. Nel caso viene configurato anche come load
balancer, in modo da distribuire il carico di lavoro su più server Gunicorn.

`Gunicorn` svolge il compito di server vero e proprio. Noto anche come "Green Unicorn", è un server WSGI (Web Server
Gateway Interface) utilizzato per eseguire applicazioni Django. Prende in carico l'esecuzione del codice dell'
applicazione e gestisce le richieste dai client, consentendo a Django di concentrarsi solo sulla logica. Gunicorn è noto
per la sua capacità di gestire richieste in modo concorrente, rendendo l'applicazione veloce e reattiva.
