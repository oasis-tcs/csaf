# Proposal 1 — Event-/Digest-Schema

*[Read this page in English](01-event-schema.md)* — dies ist eine wortgetreue, vollständige
Übersetzung des englischen Originaldokuments. Im Zweifelsfall ist die englische Fassung maßgeblich.

**Status:** Skizze, noch kein Spec-Textvorschlag. Siehe [../README.de.md](../README.de.md) für
Motivation und Einordnung gegenüber den anderen drei Proposals.

**Abhängigkeiten:** Keine. Eigenständig nutzbar, unabhängig davon ob Push (P2) je umgesetzt wird —
könnte auch als zusätzliches Feld in ROLIE-Feed-Einträgen oder `changes.csv` landen.

## Ziel

Ein kompaktes, maschinenlesbares Objekt pro Dokument-Neuveröffentlichung oder -Änderung, das die
Relevanzprüfung ermöglicht, ohne das eigentliche CSAF-Dokument zu laden.

## Vorgeschlagene Felder

- Produkt / Produktversion (Referenz auf Product-Tree-Konzepte, vermutlich `product_id` oder eine
  vergleichbare kompakte Kennung)
- Vulnerability-ID (CVE, GHSA, gCVE, herstellerspezifische ID — Bezug zu RVISC prüfen)
- Dokumenttyp (SA / SI / IA / VEX — Bezug zu den bestehenden Profilen, Abschnitt 4 der Spec)
- Status (z.B. `investigating`, `won't fix`, `fixed`, … — Bezug zu bestehendem `flags`/Remediation-
  Vokabular prüfen, nicht neu erfinden)
- Dokument-ID (zum Nachladen der Details, `tracking.id`)
- Datum
- Signatur

## Offene Fragen

- Vorrangregel bei Drift zwischen Event und Dokument: Dokument ist immer maßgeblich — wie wird das
  normativ formuliert?
- Wiederverwendung bestehender Vokabulare (Status/Flags) statt neuer Enums.
- Wo lebt das Schema strukturell — eigenes JSON-Schema, oder Erweiterung von ROLIE-Entry/`changes.csv`?

## TODO

Konkreten Spec-Text ausformulieren, sobald P1 gegenüber der TC vorgestellt und grundsätzlich positiv
aufgenommen wurde.
