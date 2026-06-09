#!/usr/bin/env python3
"""
Patientenverfuegung & Vorsorgevollmacht Dokumentengenerierung

Dieses Skript generiert aus gesammelten JSON-Daten:
1. Eine Markdown-Datei fuer die Patientenverfuegung
2. Eine Markdown-Datei fuer die Vorsorgevollmacht
3. Optional: PDF-Dateien aus den Markdown-Dateien

Nutzung:
    python3 generate_documents.py --input daten.json --output-dir ./output

Datenformat (daten.json):
{
    "name": "Max Mustermann",
    "geburtsdatum": "01.01.1970",
    "wohnort": "Berlin",
    "situationen": {
        "sterbeprozess": true,
        "wachkoma": true,
        "demenz": false,
        "weitere": false
    },
    "massnahmen": {
        "reanimation_sterbeprozess": "ablehnen",
        "beatmung_sterbeprozess": "ablehnen",
        "ernaerung_sterbeprozess": "ablehnen",
        "fluessigkeit_sterbeprozess": "ablehnen",
        "dialyse_sterbeprozess": "ablehnen",
        "antibiotika_sterbeprozess": "ablehnen",
        "reanimation_wachkoma": "ablehnen",
        "beatmung_wachkoma": "ablehnen",
        "ernaerung_wachkoma": "ablehnen",
        "fluessigkeit_wachkoma": "ablehnen",
        "dialyse_wachkoma": "ablehnen"
    },
    "weitere_situationen_text": "",
    "sterbeort": "Zuhause",
    "seelsorge": "Ja, bitte",
    "organspende": "Ja",
    "wertvorstellungen": "...",
    "vorsorgevollmacht_ort": "Im Safe",
    "bevollmaechtigte": "Erika Mustermann",
    "schweigepflicht_entbindung": "Meine Ehefrau Erika Mustermann",
    "zeugen": false,
    "bevollmaechtigte": {
        "name": "Erika Mustermann",
        "geburtsdatum": "02.02.1972",
        "wohnort": "Berlin"
    },
    "sofort_inkrafttreten": false,
    "kompetenzen": {
        "gesundheit": true,
        "vermoegen": true,
        "recht": false,
        "wohnen": true,
        "persoenlich": true
    },
    "besondere_anordnungen": "",
    "patientenverfuegung_ort": "Im Safe",
    "ersatz": null,
    "kontrollperson": null,
    "verguetung": false,
    "notar": null
}
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path

from jinja2 import Environment, FileSystemLoader


def load_template(template_dir, template_name):
    """Lade ein Jinja2-Template aus dem Verzeichnis."""
    env = Environment(loader=FileSystemLoader(template_dir))
    return env.get_template(template_name)


def render_markdown(template, data):
    """Rendere ein Template mit den uebergebenen Daten."""
    # Aktuelles Datum hinzufuegen
    data["datum"] = datetime.now().strftime("%Y-%m-%d")
    return template.render(**data)


def write_file(content, output_path):
    """Schreibe Inhalt in eine Datei."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Datei erstellt: {output_path}")
    return output_path


def generate_pdf_from_markdown(md_path, pdf_path):
    """
    Generiere eine PDF-Datei aus einer Markdown-Datei.
    Versucht verschiedene Methoden in dieser Reihenfolge:
    1. markdown + reportlab (eigene Konvertierung)
    2. weasyprint (falls verfuegbar)
    3. pandoc (falls installiert)
    """
    md_path = Path(md_path)
    pdf_path = Path(pdf_path)

    try:
        # Versuche reportlab-basierte Generierung
        return _generate_pdf_with_reportlab(md_path, pdf_path)
    except Exception as e:
        print(f"reportlab PDF-Generierung fehlgeschlagen: {e}")

    try:
        # Versuche weasyprint
        import weasyprint
        html = _markdown_to_html(md_path.read_text(encoding="utf-8"))
        weasyprint.HTML(string=html).write_pdf(str(pdf_path))
        print(f"PDF erstellt (weasyprint): {pdf_path}")
        return pdf_path
    except ImportError:
        pass
    except Exception as e:
        print(f"weasyprint PDF-Generierung fehlgeschlagen: {e}")

    try:
        # Versuche pandoc
        import subprocess
        subprocess.run(
            ["pandoc", str(md_path), "-o", str(pdf_path), "--pdf-engine=xelatex"],
            check=True,
            capture_output=True,
        )
        print(f"PDF erstellt (pandoc): {pdf_path}")
        return pdf_path
    except FileNotFoundError:
        pass
    except subprocess.CalledProcessError as e:
        print(f"pandoc PDF-Generierung fehlgeschlagen: {e.stderr.decode()}")

    print("WARNUNG: Keine PDF-Generierung moeglich. Markdown-Datei wurde erstellt.")
    return None


def _markdown_to_html(md_text):
    """Konvertiere Markdown zu einfachem HTML fuer weasyprint."""
    import markdown
    md = markdown.Markdown(extensions=["tables"])
    html_body = md.convert(md_text)
    return f"""
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {{ font-family: 'DejaVu Sans', Arial, sans-serif; margin: 2cm; line-height: 1.6; }}
            h1 {{ color: #2c3e50; border-bottom: 2px solid #2c3e50; padding-bottom: 0.3cm; }}
            h2 {{ color: #34495e; margin-top: 1cm; }}
            table {{ border-collapse: collapse; width: 100%; margin: 0.5cm 0; }}
            th, td {{ border: 1px solid #bdc3c7; padding: 0.3cm; text-align: left; }}
            th {{ background-color: #ecf0f1; }}
            blockquote {{ border-left: 4px solid #bdc3c7; padding-left: 1cm; margin-left: 0; color: #7f8c8d; }}
            code {{ background-color: #ecf0f1; padding: 0.1cm 0.2cm; }}
            hr {{ border: none; border-top: 1px solid #bdc3c7; margin: 1cm 0; }}
            ul {{ margin-left: 1cm; }}
        </style>
    </head>
    <body>
        {html_body}
    </body>
    </html>
    """


def _generate_pdf_with_reportlab(md_path, pdf_path):
    """
    Einfache PDF-Generierung mit reportlab.
    Konvertiert Markdown-Strukturen in PDF-Elemente.
    """
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import cm
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
    )
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_LEFT, TA_CENTER
    import re

    md_text = md_path.read_text(encoding="utf-8")
    # Entferne YAML-Frontmatter
    md_text = re.sub(r'^---.*?---\s*', '', md_text, flags=re.DOTALL)

    doc = SimpleDocTemplate(
        str(pdf_path),
        pagesize=A4,
        rightMargin=2 * cm,
        leftMargin=2 * cm,
        topMargin=2 * cm,
        bottomMargin=2 * cm,
    )

    styles = getSampleStyleSheet()
    # Benutzerdefinierte Stile
    styles.add(ParagraphStyle(
        name='CustomHeading1',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=colors.HexColor('#2c3e50'),
        spaceAfter=12,
        spaceBefore=12,
    ))
    styles.add(ParagraphStyle(
        name='CustomHeading2',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#34495e'),
        spaceAfter=10,
        spaceBefore=10,
    ))
    styles.add(ParagraphStyle(
        name='CustomBody',
        parent=styles['BodyText'],
        fontSize=10,
        leading=14,
        spaceAfter=6,
    ))
    styles.add(ParagraphStyle(
        name='CustomBullet',
        parent=styles['CustomBody'],
        leftIndent=20,
        bulletIndent=10,
        bulletFontSize=10,
    ))

    story = []
    lines = md_text.strip().split('\n')
    in_table = False
    table_data = []

    for line in lines:
        stripped = line.strip()

        # Ueberschriften
        if stripped.startswith('# '):
            story.append(Paragraph(stripped[2:], styles['CustomHeading1']))
        elif stripped.startswith('## '):
            story.append(Paragraph(stripped[3:], styles['CustomHeading2']))
        elif stripped.startswith('### '):
            story.append(Paragraph(stripped[4:], styles['CustomHeading2']))
        # Horizontal rule
        elif stripped == '---':
            story.append(Spacer(1, 0.3 * cm))
        # Listen
        elif stripped.startswith('- ') or stripped.startswith('* '):
            text = stripped[2:]
            text = _escape_xml(text)
            story.append(Paragraph(f"• {text}", styles['CustomBullet']))
        # Checkbox-Listen
        elif stripped.startswith('- [x]') or stripped.startswith('- [ ]'):
            checked = stripped.startswith('- [x]')
            text = stripped[5:].strip()
            text = _escape_xml(text)
            checkbox = "☑" if checked else "☐"
            story.append(Paragraph(f"{checkbox} {text}", styles['CustomBullet']))
        # Tabellen
        elif '|' in stripped and not stripped.startswith('>'):
            if not in_table:
                in_table = True
                table_data = []
            # Ignoriere Trennzeilen (---)
            if not re.match(r'^\|?\s*[-:]+\s*\|', stripped):
                cells = [cell.strip() for cell in stripped.split('|') if cell.strip()]
                table_data.append(cells)
        else:
            if in_table:
                # Tabelle abschliessen
                if table_data:
                    _add_table(story, table_data, styles)
                in_table = False
                table_data = []
            # Zitate
            if stripped.startswith('> '):
                text = stripped[2:]
                text = _escape_xml(text)
                story.append(Paragraph(f"„{text}“", styles['Italic']))
            elif stripped:
                text = _escape_xml(stripped)
                story.append(Paragraph(text, styles['CustomBody']))
            else:
                story.append(Spacer(1, 0.2 * cm))

    # Letzte Tabelle abschliessen
    if in_table and table_data:
        _add_table(story, table_data, styles)

    doc.build(story)
    print(f"PDF erstellt (reportlab): {pdf_path}")
    return pdf_path


def _escape_xml(text):
    """Escaping fuer XML/HTML in reportlab."""
    text = text.replace('&', '&amp;')
    text = text.replace('<', '&lt;')
    text = text.replace('>', '&gt;')
    return text


def _add_table(story, table_data, styles):
    """Fuege eine Tabelle zum Story hinzu."""
    from reportlab.platypus import Table, TableStyle
    from reportlab.lib import colors

    if len(table_data) < 1:
        return

    # Bestimme maximale Spaltenanzahl
    max_cols = max(len(row) for row in table_data)
    # Pade Zeilen auf gleiche Laenge
    for row in table_data:
        while len(row) < max_cols:
            row.append('')

    table = Table(table_data, repeatRows=1)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#ecf0f1')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor('#2c3e50')),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#bdc3c7')),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(table)
    story.append(Spacer(1, 0.3))


def main():
    parser = argparse.ArgumentParser(
        description="Generiere Patientenverfuegung und Vorsorgevollmacht Dokumente."
    )
    parser.add_argument(
        "--input", "-i",
        required=True,
        help="Pfad zur JSON-Datei mit den gesammelten Daten."
    )
    parser.add_argument(
        "--output-dir", "-o",
        default=".",
        help="Verzeichnis fuer die Ausgabedateien (Standard: aktuelles Verzeichnis)."
    )
    parser.add_argument(
        "--templates", "-t",
        default=None,
        help="Pfad zum Templates-Verzeichnis (Standard: templates/ im Skript-Verzeichnis)."
    )
    parser.add_argument(
        "--no-pdf",
        action="store_true",
        help="Nur Markdown-Dateien erstellen, keine PDFs."
    )
    args = parser.parse_args()

    # Templates-Verzeichnis bestimmen
    if args.templates:
        template_dir = Path(args.templates)
    else:
        template_dir = Path(__file__).parent.parent / "templates"

    if not template_dir.exists():
        print(f"FEHLER: Templates-Verzeichnis nicht gefunden: {template_dir}")
        sys.exit(1)

    # Daten laden
    with open(args.input, "r", encoding="utf-8") as f:
        data = json.load(f)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Patientenverfuegung generieren
    pv_template = load_template(template_dir, "patientenverfuegung.md.j2")
    pv_md = render_markdown(pv_template, data)
    pv_md_path = output_dir / "Patientenverfuegung.md"
    write_file(pv_md, pv_md_path)

    # Vorsorgevollmacht generieren
    vv_template = load_template(template_dir, "vorsorgevollmacht.md.j2")
    vv_md = render_markdown(vv_template, data)
    vv_md_path = output_dir / "Vorsorgevollmacht.md"
    write_file(vv_md, vv_md_path)

    # PDFs generieren
    if not args.no_pdf:
        pv_pdf_path = output_dir / "Patientenverfuegung.pdf"
        generate_pdf_from_markdown(pv_md_path, pv_pdf_path)

        vv_pdf_path = output_dir / "Vorsorgevollmacht.pdf"
        generate_pdf_from_markdown(vv_md_path, vv_pdf_path)

    print("\nGenerierung abgeschlossen!")
    print(f"Markdown-Dateien: {output_dir}")
    if not args.no_pdf:
        print(f"PDF-Dateien: {output_dir}")


if __name__ == "__main__":
    main()
