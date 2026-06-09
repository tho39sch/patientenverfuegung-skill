# Patientenverfuegung & Vorsorgevollmacht Skill

## Ueberblick

Dieser Skill fuer Claude Code fuehrt dich schrittweise durch die Erstellung einer **Patientenverfuegung** und einer **Vorsorgevollmacht**.

## Features

- **Schrittweiser Dialog**: Fuehrt durch alle relevanten Fragen
- **Konsequenzen-Hinweise**: Erklaert die rechtlichen und medizinischen Folgen deiner Entscheidungen
- **Dokumentengenerierung**: Erstellt Markdown- und PDF-Dateien
- **Datenschutz**: Alles bleibt lokal in deinem Vault
- **Empathisch**: Wuerdevolle, klare Sprache

## Installation

Keine separate Installation erforderlich. Der Skill wird automatisch von Claude Code erkannt, wenn er im Verzeichnis `.claude/skills/patientenverfuegung/` liegt.

### Python-Abhaengigkeiten

Fuer die PDF-Generierung werden Python-Pakete benoetigt:

```bash
pip install jinja2 reportlab markdown
```

Alternativ (falls reportlab Probleme macht):

```bash
pip install jinja2 weasyprint markdown
```

## Nutzung

### Start

Rufe den Skill auf mit:

```
/patientenverfuegung
```

Oder beginne mit einer natuerlichen Anfrage:

- "Ich moechte eine Patientenverfuegung erstellen"
- "Hilf mir bei der Vorsorgevollmacht"

### Ablauf

1. **Willkommen** – Du erhaelst eine Einleitung zum Zweck und zur Tragweite
2. **Persoenliche Daten** – Name, Geburtsdatum, Adresse (optional)
3. **Patientenverfuegung** –
   - Auswahl der relevanten medizinischen Situationen
   - Festlegung gewuenschter/ablehnter Massnahmen pro Situation
   - Persoenliche Wertvorstellungen (Sterbeort, Seelsorge, Organspende)
4. **Vorsorgevollmacht** –
   - Bevollmaechtigte (Name, Beziehung)
   - Kompetenzbereiche (Gesundheit, Finanzen, Wohnen)
   - Ersatzbevollmaechtigte
5. **Ueberpruefung** – Zusammenfassung aller Angaben
6. **Generierung** – Speicherung als Markdown und PDF

### Konsequenzen-Hinweise

Waehrend des Dialogs wirst du bei wichtigen Entscheidungen auf Konsequenzen hingewiesen, z.B.:

- Was bedeutet die Ablehnung kuenstlicher Ernaehrung im Wachkoma?
- Was passiert, wenn keine Vorsorgevollmacht vorliegt?
- Wie verbindlich ist die Patientenverfuegung?

### Speicherort

Die generierten Dokumente werden standardmaessig in `160_Private_Org/` gespeichert. Du kannst einen anderen Ort waehlen.

## Wichtige Hinweise

### Rechtliche Verbindlichkeit

- Die **Patientenverfuegung** ist nach § 1827 BGB fuer Aerzte und Pflegepersonal verbindlich (sofern konkret formuliert).
- Die **Vorsorgevollmacht** ermoeglicht es einer Vertrauensperson, in deinem Namen zu entscheiden.
- Ohne diese Dokumente entscheidet das Betreuungsgericht ueber einen Betreuer.

### Schriftform

- Beide Dokumente muessen **schriftlich** und **eigenhaendig unterschrieben** werden.
- Eine notarielle Beurkundung ist nicht zwingend, aber bei komplexen Faellen empfohlen.
- Lass dich von einem Notar oder Rechtsanwalt beraten.

### Aktualisierung

Ueberpruefe deine Vorsorgedokumente regelmaessig (alle 2–3 Jahre) oder bei:
- Aenderung deiner Lebenssituation
- Neue Erkenntnisse ueber deine Gesundheit
- Tod oder Veraenderung der Bevollmaechtigten

## Dateien

- `SKILL.md` – Skill-Definition fuer Claude Code
- `templates/patientenverfuegung.md.j2` – Template fuer Patientenverfuegung
- `templates/vorsorgevollmacht.md.j2` – Template fuer Vorsorgevollmacht
- `scripts/generate_documents.py` – Python-Skript zur Generierung

## Support

Bei Fragen oder Problemen:
1. Pruefe, ob Python 3.x installiert ist: `python --version`
2. Pruefe die Abhaengigkeiten: `pip list | grep -E "jinja2|reportlab|markdown"`
3. Oeffne das Projekt in Obsidian und pruefe den Vault-Pfad

## Lizenz

Privater Skill fuer den persoenlichen Gebrauch im Obsidian Vault.
