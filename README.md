# Metzgerei_Backend

19.02.2025:
Models erstellt:
1. Mitarbeiter:
   id (AutoIncrease)
   firstname (Char)
   lastname (Char)
   gehalt (Decimal, überlegung mit Float zu arbeiten laut Recherche kann dies aber zu Rechenfehlern führen)
   schichtzeiten (Char)
   postion (Char)

2. Artikel
  id(AutoIncrease)
  artikelnummer (Int)
  beschreibung (Char)
  lagerbestand (Int)

3. Pferd
   id (AutoIncrease)
   name (Char)
   gewicht (Float absichtlich verwendet zur Prüfung, ob eine Komplikation bei Rechnungen entsteht)
   herkunft (Char)

Erweiterung eventuell notwendig... Achtung führt ebenfalls zur Anpassung der dato erstellten Serializer, weil alle fields einzeln angegeben worden sind.
Erstellung der Serializer anhand der bisherigen Tabellenstruktur
Erstellung je 2 Views einer zur Bearbeitung und einer für die View Only
Offen: Permission classes
Urls: In Api und in App eingefügt
Admin Panel hat die Möglichkeit erhalten Daten in den Tabellen einzutragen
Installed Apps sind alle wichtigen Dinge hinzugefügt

To Do:
Middleware
Frontend -> Evenutell mit React erstellen?

Frontend:
https://htmx.org/
