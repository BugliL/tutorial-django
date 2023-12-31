# Tutorial Django
Tutorial che spiega le caratteristiche principali di DJango.
Lo scopo e' quello di imparare aspetti avanzati specifici e base ad ampio campo che difficilmente sono trattati in
tutorial base.

## Le origini di Django
Il framework è stato sviluppato da Adrian Holovaty e Simon Willison mentre lavoravano per il quotidiano Lawrence 
Journal-World. Inizialmente, avevano la necessità di creare applicazioni web complesse e performanti per gestire 
notizie e contenuti giornalistici. Per semplificare questo processo, hanno sviluppato un insieme di strumenti, 
il nucleo di Django.


## Gli aspetti principali di Django
1. **Model-View-Template (MVT) Architecture**
    Il model rappresenta i dati dell'applicazione, la view gestisce la logica di presentazione e il template definisce 
    l'aspetto dell'interfaccia utente. 

    **Problemi legati a questa feature**
    Questo tipo di architettura porta a gonfiare i modelli con la logica e a tenere molto snelle le view. 

    **Miglioria**: introduzione di un livello di servizio che si occupa della logica di business a partire dai modelli.

2. **Object-Relational Mapping (ORM)**
    Il tipo di pattern e' [Active record](https://en.wikipedia.org/wiki/Active_record_pattern), consiste nell'incapsulare
    una tabella del database in una classe, in modo che ogni istanza della classe rappresenti una singola riga della
    tabella.

    **Problemi legati a questa feature**
    - *Rigidezza del database*: legame stretto tra le classi del modello e la struttura del database, rendendo difficile 
      apportare modifiche complesse alla base di dati o gestire schemi in evoluzione.

    - *Complessità dei dati*: Con modelli di dati complessi e relazioni tra entità può portare a codice duplicato e 
      difficoltà di gestione, specialmente quando si devono gestire strutture dati intricate.

    - *Violazione principio singola responsabilità*: assegna sia la logica dell'applicazione che l'interazione con il 
      database alle classi del modello, creando classi sovraccariche e meno manutenibili. Questo contrasta con il principio 
      di singola responsabilità, che suggerisce che una classe dovrebbe avere una sola ragione per essere modificata.

    **Miglioria**: introduzione di un livello di servizio che si occupa della logica di business a partire dai modelli.


3. **Admin Interface generata automaticamente**
    Sono delle interfacce di gestione dei dati utilizzate dagli utenti staff che vengono generate automaticamente a 
    partire dai modelli. Gli utenti di staff sono in grado di gestire i dati attraverso queste interfacce senza scrivere 
    codice.

    **Problemi legati a questa feature**
    Poca personalizzazione sia da un punto di vista visuale che da un punto di vista funzionale.

## Prerequisiti
Per far funzionare il progetto serve `python3.10+` e `poetry`.  
```shell
poetry install
```

### Spiegazione dei singoli pacchetti

**Django REST Framework (djangorestframework)**
Framework completo per lo sviluppo di API Web in Django. Fornisce strumenti e funzionalità avanzate per creare,
serializzare, deserializzare e gestire le richieste API REST. Django REST Framework semplifica il processo di creazione
di API robuste, consentendo di gestire l'autenticazione, l'autorizzazione, la validazione dei dati e molto altro.

**Django Debug Toolbar (django-debug-toolbar)**
Fornisce una barra degli strumenti interattiva per il debug delle applicazioni Django. Mostra informazioni utili sulle
query del database eseguite, i tempi di caricamento delle pagine, i messaggi di debug e altro ancora. La barra degli
strumenti semplifica l'analisi delle prestazioni e l' individuazione di eventuali problemi o inefficienze nel codice.

**Django rest framework - Yet Another Swagger Generator (drf-yasg)**
Offre un'interfaccia interattiva di documentazione per le API Django REST Framework utilizzando lo standard Swagger.
Drf-yasg fornisce una documentazione chiara e intuitiva per le API.