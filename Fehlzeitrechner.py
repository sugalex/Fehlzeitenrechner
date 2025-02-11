from datetime import date, datetime, timedelta
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO


class FehlzeitenRechner:
    def __init__(self, root):
        self.root = root
        self.root.title("Fehlzeitenrechner")

        # Logo von URL laden und anzeigen
        try:
            # Logo von URL laden
            logo_url = "https://portal.cc-student.com/gfx/site/header/logo_college.png"
            response = requests.get(logo_url)
            image = Image.open(BytesIO(response.content))

            # Fensterbreite basierend auf Logobreite berechnen (plus Rand)
            padding = 40  # 20 Pixel Rand auf jeder Seite
            window_width = image.width + padding
            self.root.geometry(f"{window_width}x600")

            # Logo ohne Größenanpassung konvertieren
            self.logo = ImageTk.PhotoImage(image)

            # Logo-Label erstellen und platzieren
            logo_label = tk.Label(self.root, image=self.logo)
            logo_label.pack(pady=10)
        except Exception as e:
            print(f"Fehler beim Laden des Logos: {e}")

        # Feiertage Liste (unverändert)
        self.feiertage = [
            date(2024, 12, 24),  # Heiligabend
            date(2024, 12, 25),  # Erster Weihnachtstag
            date(2024, 12, 26),  # Zweiter Weihnachtstag
            date(2024, 12, 31),  # Silvester
            date(2025, 1, 1),  # Neujahr
            date(2025, 3, 29),  # Beispiel-Feiertag
        ]
        # GUI Elemente erstellen
        self.create_widgets()

    def create_widgets(self):
        # Styling
        padding = {'padx': 10, 'pady': 5}

        # Datum Eingabe
        ttk.Label(self.root, text="Abschlussprüfung (DD.MM.YYYY):").pack(**padding)
        self.datum_entry = ttk.Entry(self.root)
        self.datum_entry.pack(**padding)

        # Gesamttage Eingabe
        ttk.Label(self.root, text="Erfasste Gesamttage:").pack(**padding)
        self.gesamt_entry = ttk.Entry(self.root)
        self.gesamt_entry.pack(**padding)

        # Aktuelle Quote Eingabe
        ttk.Label(self.root, text="Aktuelle Fehlzeitenquote (%):").pack(**padding)
        self.quote_entry = ttk.Entry(self.root)
        self.quote_entry.pack(**padding)

        # Zielquote Eingabe
        ttk.Label(self.root, text="Gewünschte Zielquote (%):").pack(**padding)
        self.ziel_entry = ttk.Entry(self.root)
        self.ziel_entry.pack(**padding)

        # Berechnen Button
        ttk.Button(self.root, text="Berechnen", command=self.calculate).pack(**padding)

        # Ergebnis Anzeige
        self.result_text = tk.Text(self.root, height=8, width=40)
        self.result_text.pack(**padding)

    def calculate(self):
        try:
            # Eingaben verarbeiten
            enddatum = datetime.strptime(self.datum_entry.get(), "%d.%m.%Y").date()
            gesamt_tage = int(self.gesamt_entry.get())
            fehlzeiten_quote = float(self.quote_entry.get().replace(',', '.'))
            ziel_quote = float(self.ziel_entry.get().replace(',', '.'))

            # Berechnungen durchführen
            ab_heute = date.today()
            arbeitstage = self.berechne_vorausrechner(ab_heute, enddatum)
            fehltage_gesamt = self.berechne_hauptrechner(gesamt_tage, fehlzeiten_quote)
            zusatz_tage = self.berechne_rueckwaertsrechner(gesamt_tage, fehltage_gesamt, ziel_quote)

            # Ergebnisse anzeigen
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END,
                                    f"Heutiges Datum: {ab_heute}\n"
                                    f"Schultage bis Prüfung: {abs(arbeitstage)}\n"
                                    f"Aktuelle Fehltage: {fehltage_gesamt}\n"
                                    )

            if zusatz_tage > 0:
                self.result_text.insert(tk.END,
                                        f"\nDu musst {zusatz_tage} zusätzliche Tage\n"
                                        f"ohne Fehlzeiten zur Schule kommen,\n"
                                        f"um die gewünschte Quote zu erreichen."
                                        )
            else:
                self.result_text.insert(tk.END,
                                        "\nDu hast die gewünschte Fehlzeitenquote\n"
                                        "bereits erreicht oder unterschritten."
                                        )

        except ValueError as e:
            messagebox.showerror("Fehler", "Bitte überprüfe deine Eingaben!")

    def berechne_vorausrechner(self, startdatum, enddatum):
        arbeitstage = 0
        current_date = startdatum

        while current_date <= enddatum:
            if current_date.weekday() < 5 and current_date not in self.feiertage:
                arbeitstage += 1
            current_date += timedelta(days=1)

        return arbeitstage

    def berechne_hauptrechner(self, gesamt_tage, fehlzeiten_quote):
        return gesamt_tage * (fehlzeiten_quote / 100)

    def berechne_rueckwaertsrechner(self, gesamt_tage, fehltage_gesamt, ziel_quote):
        aktuelle_quote = (fehltage_gesamt / gesamt_tage) * 100
        if aktuelle_quote <= ziel_quote:
            return 0

        zusatz_tage = 0
        while (fehltage_gesamt / (gesamt_tage + zusatz_tage)) * 100 > ziel_quote:
            zusatz_tage += 1

        return zusatz_tage


# Hauptprogramm
if __name__ == "__main__":
    root = tk.Tk()
    app = FehlzeitenRechner(root)
    root.mainloop()