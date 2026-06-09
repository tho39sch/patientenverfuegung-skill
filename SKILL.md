---
name: patientenverfuegung
description: Skill zur schrittweisen Erstellung einer Patientenverfuegung und Vorsorgevollmacht. Fuehrt durch einen empathischen, strukturierten Dialog, klaert offene Fragen, weist auf Konsequenzen hin und generiert am Ende Markdown- und PDF-Dokumente.
---

# Patientenverfuegung & Vorsorgevollmacht Skill

Dieser Skill hilft bei der Erstellung einer **Patientenverfuegung** (§ 1827 BGB) und einer **Vorsorgevollmacht** nach deutschem Recht.

## Wichtiger Hinweis

> [!warning] Keine Rechtsberatung
> Dieser Skill erstellt strukturierte Vorlagen. Fuer rechtsverbindliche Dokumente wird dringend empfohlen, einen Notar oder Rechtsanwalt hinzuzuziehen.

## Nutzung

Rufe den Skill auf mit:
```
/patientenverfuegung
```

Oder starte direkt mit:
- "Ich moechte eine Patientenverfuegung erstellen"
- "Hilf mir bei der Vorsorgevollmacht"

## Ablauf

### Phase 1: Willkommen & Einleitung

Frage den Nutzer freundlich, ob er eine Patientenverfuegung, eine Vorsorgevollmacht oder beides erstellen moechte.

Erklaere kurz:
- Was ist eine Patientenverfuegung? (Festlegung medizinischer Wuensche fuer den Fall der Einwilligungsunfaehigkeit)
- Was ist eine Vorsorgevollmacht? (Uebertragung der Entscheidungsbefugnis an eine Vertrauensperson)
- Warum beides zusammen wichtig ist (Patientenverfuegung = WAS, Vorsorgevollmacht = WER entscheidet)

> [!info] Hinweis
> Beide Dokumente sollten zusammen erstellt werden, damit die Bevollmaechtigte Person die medizinischen Wuensche durchsetzen kann.

### Phase 2: Persoenliche Daten

Sammle folgende Informationen (optional, kann uebersprungen werden):

1. **Name, Vorname**
2. **Geburtsdatum**
3. **Wohnort / Adresse**

> [!tip] Datenschutz
> Alle Daten werden ausschliesslich lokal in deinem Vault gespeichert. Es findet keine Uebertragung an externe Server statt.

### Phase 3: Patientenverfuegung

Fuehre den Nutzer durch einen strukturierten Dialog. Stelle **eine Frage nach der anderen** und warte auf die Antwort.

#### 3.1 Medizinische Situationen auswaehlen

Frage den Nutzer, fuer welche Situationen er Vorsorge treffen moechte. Zeige die Optionen als Liste:

- **Unmittelbarer Sterbeprozess** (ausweglos, Tod bevorstehend)
- **Dauerhafte Bewusstlosigkeit** (Wachkoma, apallisches Syndrom)
- **Fortgeschrittene Demenz** (Verlust von Persoenlichkeit und Einsicht)
- **Weitere eigene Situationen** (z.B. spezifische Erkrankung)

**Konsequenzen-Hinweis:**
> [!warning] Wichtig
> Die Patientenverfuegung muss fuer jede Situation **konkret** formuliert sein. Pauschale Aussagen wie "keine kuenstliche Ernaehrung" genuegen rechtlich nicht.

#### 3.2 Massnahmen pro Situation festlegen

Fuer jede ausgewaehlte Situation frage nach folgenden Massnahmen:

| Massnahme | Optionen |
|------------|----------|
| Wiederbelebung (Reanimation) | ablehnen / wuenschen / nach aerztlichem Ermessen |
| Kuenstliche Beatmung | ablehnen / wuenschen / nach aerztlichem Ermessen |
| Kuenstliche Ernaehrung (PEG-Sonde) | ablehnen / wuenschen / nach aerztlichem Ermessen |
| Kuenstliche Fluessigkeitszufuhr | ablehnen / wuenschen / nach aerztlichem Ermessen |
| Dialyse | ablehnen / wuenschen / nach aerztlichem Ermessen |
| Antibiotika | ablehnen / wuenschen / nach aerztlichem Ermessen |
| Bluttransfusionen | ablehnen / wuenschen / nach aerztlichem Ermessen |

**Konsequenzen-Hinweise bei Ablehnung:**
- **Kuenstliche Ernaehrung:** Sollte diese abgelehnt werden, fuehrt dies bei Bewusstlosigkeit zum Verhungern/Verdursten. Die Entscheidung ist rechtlich zulaessig, aber ethisch schwerwiegend.
- **Wiederbelebung:** Sollte diese abgelehnt werden, wird im Notfall keine Reanimation durchgefuehrt. Dies ist endgueltig.
- **Beatmung:** Ohne Beatmung kann der Tod schneller eintreten, falls die Atmung versagt.

**Bei jedem Punkt hinweisen:**
> [!note] Schmerzbehandlung
> Unabhaengig von der Entscheidung zu lebensverlaengernden Massnahmen: Eine fachgerechte Schmerz- und Symptombehandlung wuensche ich in jedem Fall.

#### 3.3 Persoenliche Wuensche

Frage nach:

1. **Bevorzugter Sterbeort:** Zuhause, Hospiz, Krankenhaus, wunschlos
2. **Seelsorge / Begleitung:** Ja / Nein / Falls gewuenscht
3. **Organspende:** Ja (Ausweis vorhanden?) / Nein / Unentschieden
4. **Entbindung von der Schweigepflicht:** Fuer wen? (Ehepartner, Kinder, etc.)

#### 3.4 Persoenliche Wertvorstellungen (optional)

Frage nach Wertvorstellungen, die als Auslegungshilfe dienen koennen:

> Beispiel: "Mein Leben hat Sinn, solange ich meine Umgebung wahrnehmen und mit Menschen kommunizieren kann."

### Phase 4: Vorsorgevollmacht

#### 4.1 Bevollmaechtigte Person

Sammle:
- Name, Vorname
- Geburtsdatum
- Wohnort
- Beziehung zum Nutzer

> [!warning] Konsequenz
> Ohne Vorsorgevollmacht bestellt das Betreuungsgericht einen Betreuer – moeglicherweise eine dir fremde Person. Mit Vorsorgevollmacht bestimmst du selbst, wer fuer dich entscheidet.

#### 4.2 Kompetenzbereiche

Frage fuer welche Bereiche die Vollmacht erteilt werden soll:

- [ ] **Gesundheitssorge** (Aerzte, Behandlungen, Pflege, Patientenverfuegung durchsetzen)
- [ ] **Vermoegenssorge** (Bank, Miete, Steuern, Sozialleistungen)
- [ ] **Rechtssorge** (Prozesse, Anwaelte, Behoerden)
- [ ] **Wohnungs- und Aufenthaltssorge** (Wohnsitz, Pflegeheim, Umzug)
- [ ] **Persoenliche Angelegenheiten** (Besuche, Kommunikation)

**Konsequenzen-Hinweis:**
> [!info] Gesundheitssorge
> Dies ist der wichtigste Bereich fuer die Durchsetzung der Patientenverfuegung. Ohne Gesundheitsvollmacht kann der Bevollmaechtigte nicht ueber Behandlungen entscheiden.

#### 4.3 Weitere Festlegungen

- **Sofortiges Inkrafttreten:** Ja / Nein (Standard: erst bei Geschaeftsunfaehigkeit)
- **Ersatzbevollmaechtigte:** Name und Daten einer Ersatzperson
- **Kontrollperson:** Jemand, der die Taetigkeit der Bevollmaechtigten ueberwacht
- **Verguetung:** Soll die Bevollmaechtigte eine Verguetung erhalten?

#### 4.4 Besondere Anordnungen (optional)

Frage nach besonderen Wuenschen:
- Einzelzimmer in der Pflege
- Kein bestimmtes Heim
- Wunsch, zu Hause zu bleiben
- etc.

### Phase 5: Ueberpruefung

Erstelle eine **Zusammenfassung** aller Angaben:

- Persoenliche Daten
- Ausgewaehlte Situationen und Massnahmen
- Bevollmaechtigte Person und Kompetenzen
- Besondere Wuensche

Frage den Nutzer:
> "Bitte ueberpruefe die Zusammenfassung. Moechtest du etwas aendern, oder soll ich die Dokumente generieren?"

Biete Optionen:
- Korrekturmoeglichkeiten
- Fortfahren zur Generierung

### Phase 6: Dokumentengenerierung

1. Erstelle ein JSON mit allen gesammelten Daten
2. Rufe das Python-Skript auf:
   ```bash
   python3 .claude/skills/patientenverfuegung/scripts/generate_documents.py -i daten.json -o ZIELVERZEICHNIS -t .claude/skills/patientenverfuegung/templates
   ```
3. Zeige dem Nutzer die erstellten Dateien
4. Erklaere die naechsten Schritte:
   - Ausdrucken
   - Eigenhaendig unterschreiben
   - Notarielles Beglaubigen (optional, empfohlen)
   - Aufbewahrung (Safe, Zentrales Vorsorgeregister)
   - Angehoerige informieren

> [!warning] Wichtig
> Die generierten Dokumente muessen **ausgedruckt und eigenhaendig unterschrieben** werden. Eine digitale Unterschrift reicht nicht aus. Die Schriftform ist zwingend erforderlich (§ 1827 BGB).

## Technische Details

### Dateien

- `SKILL.md` – Diese Datei
- `README.md` – Nutzeranleitung
- `templates/patientenverfuegung.md.j2` – Jinja2-Template fuer Patientenverfuegung
- `templates/vorsorgevollmacht.md.j2` – Jinja2-Template fuer Vorsorgevollmacht
- `scripts/generate_documents.py` – Python-Skript zur Generierung

### Datenschutz

- Keine Cloud-Speicherung
- Lokale Generierung im Vault
- JSON-Daten werden nach Generierung geloescht (oder vom Nutzer aufbewahrt)

### Abhaengigkeiten

- Python 3.x
- jinja2 (`pip3 install jinja2`)
- reportlab (`pip3 install reportlab`)
- markdown (`pip3 install markdown`)

## Empathie-Richtlinien

- Sprache ist **wuerdevoll, klar und nicht dramatisierend**
- Keine Entscheidungsdringlichkeit erzeugen
- Pausen ermoeglichen ("Du kannst jederzeit Pause machen und spaeter fortfahren")
- Bei Ablehnung lebensverlaengernder Massnahmen: Hinweis auf Schmerzbehandlung
- Respektvoller Umgang mit religioesen und ethischen Ueberzeugungen
- Keine Wertung der Entscheidungen

## Fehlerbehandlung

Falls das Python-Skript fehlschlaegt:
1. Pruefe, ob Python 3 installiert ist: `python3 --version`
2. Pruefe Abhaengigkeiten: `python3 -c "import jinja2, reportlab, markdown; print('OK')"`
3. Fehlende Pakete installieren: `pip3 install jinja2 reportlab markdown`
4. Alternativ nur Markdown-Dateien erstellen: `--no-pdf` Flag verwenden

## Beispiel-Durchlauf

**Nutzer:** "Ich moechte eine Patientenverfuegung erstellen"

**Claude:**
> Hallo! Ich helfe dir gerne bei der Erstellung einer Patientenverfuegung und Vorsorgevollmacht.
>
> Die **Patientenverfuegung** legt fest, welche medizinischen Massnahmen du wuenschst oder ablehnst, wenn du nicht mehr entscheiden kannst.> Die **Vorsorgevollmacht** bestimmt, **wer** in deinem Namen entscheidet, wenn du es nicht mehr kannst.>
> Beide Dokumente ergaenzen sich ideal. Sollen wir beide zusammen erstellen?
>
> **Wichtig:** Ich erstelle strukturierte Vorlagen. Fuer rechtsverbindliche Dokumente empfehle ich, einen Notar oder Rechtsanwalt hinzuzuziehen.

**Nutzer:** "Ja, beide bitte"

**Claude:**
> Perfekt. Beginnen wir mit deinen persoenlichen Daten. Du kannst auch "ueberspringen" sagen, wenn du die Daten erst spaeter eintragen moechtest.
>
> **Wie ist dein Name?**

**Nutzer:** "Max Mustermann"

**Claude:**
> Danke, Max. **Dein Geburtsdatum?**

... und so weiter durch alle Phasen.
