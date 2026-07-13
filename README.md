# AnchayShop — E-commerce PPM 2026

## Studente
Sherwin Andre Anchay Ttito

## Matricola
7133335

## Tipo di progetto
Full-Stack Web Application

## Framework
Django 4.x

## Descrizione
AnchayShop è un e-commerce completo che permette agli utenti di navigare un catalogo prodotti,aggiungere articoli al carrello e completare ordini. 
I manager possono gestire prodotti,categorie e ordini tramite una dashboard dedicata.

## Funzionalità per ruolo

### Customer
- Registrazione e login
- Navigazione catalogo con ricerca e filtro per categoria
- Pagina di dettaglio prodotto
- Gestione carrello (aggiungi/rimuovi prodotti)
- Creazione ordini
- Visualizzazione storico ordini personali

### Store Manager
- Tutte le funzionalità del Customer
- Dashboard di gestione prodotti e ordini
- Creazione, modifica ed eliminazione prodotti
- Visualizzazione di tutti gli ordini ricevuti

### Admin (Superuser)
- Accesso al pannello Django Admin
- Gestione completa di utenti, prodotti, categorie e ordini

## Installazione locale

```bash
git clone https://github.com/SherwinAnchay/ecommerce-ppm.git
cd ecommerce-ppm
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
pip install -r requirements.txt
python manage.py migrate
python populate_db.py
python manage.py runserver
```

Apri il browser su: http://127.0.0.1:8000

## Database
Il file `db.sqlite3` è incluso nel repository ed è pre-popolato con categorie,
prodotti e account demo pronti per essere testati.

## Account demo

| Username | Password | Ruolo |
|---|---|---|
| admin_demo | admin12345 | Superuser / Admin |
| manager_demo | manager12345 | Store Manager |
| user_demo | user12345 | Customer |

## Scenario di test consigliato

1. Accedere con `user_demo` / `user12345`
2. Navigare il catalogo e filtrare per categoria
3. Aggiungere prodotti al carrello
4. Concludere l'ordine e verificare lo storico ordini
5. Uscire e accedere con `manager_demo` / `manager12345`
6. Aprire la Dashboard Manager
7. Creare un nuovo prodotto, modificarlo ed eliminarlo
8. Visualizzare gli ordini ricevuti
9. Provare ad accedere alla Dashboard Manager con `user_demo` per verificare che venga negato l'accesso (aggiungere "/manager/" alla fine del link)

## Deployment
https://ecommerce-ppm-b8iv.onrender.com  