# Proposal 3 — Kanal-Autorisierung (TLP-/Sharing-Group-Gate)

*[Read this page in English](03-channel-authorization.md)* — dies ist eine wortgetreue, vollständige
Übersetzung des englischen Originaldokuments. Im Zweifelsfall ist die englische Fassung maßgeblich.

**Status:** Skizze, noch kein Spec-Textvorschlag. Siehe [../README.de.md](../README.de.md) für
Motivation und Einordnung gegenüber den anderen drei Proposals.

**Abhängigkeiten:** Setzt P2 (oder zumindest einen Push-/Zugriffs-Mechanismus) voraus, um überhaupt
etwas zu gaten. Nutzt ausschließlich bereits bestehende Dokumentfelder.

## Ziel

Ein Kanal pro Produkt statt ein Kanal pro TLP-Stufe. Zustellung eines Events/Dokuments nur an
Subscriber, deren Berechtigung dem `distribution.tlp.label` bzw. der `distribution.sharing_group.id`
des Dokuments entspricht.

## Eckpunkte

- TLP:RED verlässt den Distributionsmechanismus nie (interne Vorarbeit, kein Kanalthema).
- TLP:AMBER → Sharing-Group-gebunden, zeitlich befristet (Embargo-Karenz ist ein Prozess-/
  Governance-Thema, kein neues Pflichtfeld — außer die TC möchte ein maschinenlesbares "geplantes
  Freigabedatum" ergänzen, siehe offene Fragen).
- TLP:GREEN/CLEAR → offen, keine Autorisierung nötig.
- Gestaffelte gestufte Freigabe (RED → AMBER → GREEN) = neue Revision desselben Dokuments zu höherer
  TLP-Stufe, kein separates Dokument/Kanalwechsel-Konzept.

## Bewusste Abgrenzung

Die Spec schreibt vor, **dass** eine Autorisierungsentscheidung auf `tlp`/`sharing_group` beruhen
muss — **nicht wie** authentifiziert wird (kein Zwang zu einem bestimmten Auth-Protokoll/Token-Format).
Analog zu Requirement 3 (TLS wird vorgeschrieben, die Zertifikatswahl bleibt offen).

## Offene Fragen

- Maschinenlesbares "geplantes Freigabedatum" für AMBER-Dokumente — echter Neuzugang, noch nicht
  vorhanden. Getrennt von der reinen Kanal-Frage zu bewerten.
- Konsistenzanforderung: Rekonziliationsquelle (P1/P2) für eine TLP-Stufe muss denselben Schutz haben
  wie der zugehörige Push-Kanal.

## TODO

Konkreten Spec-Text (vermutlich Ergänzung zu Abschnitt 7.1/7.2 sowie ggf. Klarstellung in 3.2.2.5)
ausformulieren.
