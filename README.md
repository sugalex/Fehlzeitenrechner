# **Fehlzeitenrechner mit Python** 🧮📅<br>
Com.cave Fehltagerechner, für alle die ein Problem mit ihren Fehlzeiten haben

In der Schule wird jede Minute als Fehlzeit gezählt. Sobald sich 10 % Fehlzeiten angesammelt haben, wird man von der Teilnahme an der IHK-Prüfung ausgeschlossen. Mit diesem Rechner gibt man die verbleibenden Tage bis zur IHK-Prüfung sowie die aktuelle Fehlzeit-Prozentzahl und die angestrebte Prozentzahl ein. Der Rechner gibt daraufhin aus, wie viele Tage man in Folge anwesend sein muss, um die angestrebte Prozentzahl zu erreichen. Dabei werden nur die Arbeitstage berücksichtigt, nicht die Wochenenden.

### Features ✨<br>
Berechnet die erforderlichen Anwesenheitstage basierend auf aktuellen und gewünschten Fehlzeiten

✨ Berücksichtigt Feiertage

✨ Benutzerfreundliches GUI mit Tkinter

✨ Einfache Eingabe von Daten

✨ Visuelle Darstellung der Ergebnisse

**Benötigte pip-Pakete:**<br>
Pillow<br>
Wird für das Laden und Anzeigen von Bildern (z. B. das Logo) verwendet.<br>
```pip install Pillow ```

Requests:<br>
Wird verwendet, um das Bild über eine URL herunterzuladen.<br>
```pip install requests ```


Feiertage manuell eintragen 🎉📆
In diesem Code-Abschnitt werden alle Feiertage manuell eingetragen. Diese Feiertage werden später bei der Berechnung der Anwesenheitstage berücksichtigt, um sicherzustellen, dass nur die tatsächlichen Arbeitstage gezählt werden.
# Feiertage manuell eintragen 
```python
self.feiertage = 
[
    date(2024, 12, 24),  # Heiligabend
    date(2024, 12, 25),  # Erster Weihnachtstag
    date(2024, 12, 26),  # Zweiter Weihnachtstag
    date(2024, 12, 31),  # Silvester
    date(2025, 1, 1),    # Neujahr
    date(2025, 3, 29),   # Beispiel-Feiertag
]
```
![image](https://github.com/user-attachments/assets/27e36b2c-6b6b-410b-8266-c661a98ee109)

