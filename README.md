# puhelin-arvostelut

## Sovelluksen toiminnot

* Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
* Käyttäjä pystyy lisäämään, muokkaamaan ja poistamaan arvosteluja.
* Käyttäjä pystyy lisäämään kuvia arvosteluun.
* Käyttäjä näkee sovellukseen lisätyt arvostelut.
* Käyttäjä pystyy etsimään arvosteluja hakusanalla.
* Sovelluksessa on käyttäjäsivut, jotka näyttävät tilastoja ja käyttäjän lisäämät arvostelut.
* Käyttäjä pystyy valitsemaan arvostelulle yhden tai useamman luokittelun (käyttöjärjestelmä, tuottaja).
* Käyttäjä pystyy jättämään kommentin arvosteluun.

## Sovelluksen asennus

Kloonaa sovellus:

```
$ git clone https://github.com/riicgz/puhelin-arvostelut.git
```

Luo virtuaaliympäristö:

```
$ python3 -m venv venv
$ source venv/bin/activate
```


Asenna `flask`-kirjasto:

```
$ pip install flask
```

Luo tietokannan taulut:

```
$ sqlite3 database.db < schema.sql
$ sqlite3 database.db < init.sql
```

Voit käynnistää sovelluksen näin:

```
$ flask run
```
