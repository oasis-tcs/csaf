# Proposal 4 — Delegierte Publikation (Proxy Trusted Provider + Provenienzkette)

*[Read this page in English](04-delegated-publication.md)* — dies ist eine wortgetreue, vollständige
Übersetzung des englischen Originaldokuments. Im Zweifelsfall ist die englische Fassung maßgeblich.

**Status:** Skizze, noch kein Spec-Textvorschlag. Siehe [../README.de.md](../README.de.md) für
Motivation und Einordnung gegenüber den anderen drei Proposals.

**Abhängigkeiten:** Unabhängig von P1–P3, kann parallel entstehen.

## Ziel

Formalisierter, öffentlich dokumentierter Weg für Anbieter ohne eigene Hosting-/
Signatur-Infrastruktur ("dumme Datei"), über einen Trusted Provider zu publizieren — inklusive
kryptographischer Nachweiskette, dass die Publikation vom Original-Vendor autorisiert ist.

## Ausgangspunkt in der bestehenden Spec

- Das Konzept existiert bereits als **"CSAF Proxy Provider"** — aktuell aber nur Aggregator-seitig
  und ausdrücklich nicht öffentlich zugänglich (Abschnitt 7.2.5). Dieser Proposal formalisiert das
  Muster auf Trusted-Provider-Ebene und macht es zu einem dokumentierten Onboarding-Weg.
- Identitätsanker: `document.publisher.namespace` (bereits Pflichtfeld, global eindeutige URL unter
  Kontrolle des Vendors).
- Signatur-Infrastruktur: Requirements 19/20 (OpenPGP-Signatur + Public Key) bereits vorhanden.
- Präzedenzfall für Opt-in/Delegation: `list_on_CSAF_aggregators` / `mirror_on_CSAF_aggregators`.

## Zwei Varianten

**A — Vendor hat eigenen Key:** Vendor signiert Rohdatei selbst, TP übernimmt Hosting + fügt eigene
Gegensignatur als Relay-Attestierung hinzu. Consumer verifiziert beide Signaturen unabhängig.

**B — Vendor hat keinen eigenen Key:** TP signiert allein, nach einmaliger Out-of-Band-Prüfung der
Vendor-Identität beim Onboarding — analog zur bestehenden Aggregator-Regel ("If the issuing party
does not provide those files, they SHALL be created by the CSAF aggregator"). Schwächere
Nicht-Abstreitbarkeit, aber pragmatischer Fallback für die am wenigsten ausgestatteten Anbieter.

## Neu zu spezifizieren

Ein explizites, zeitlich befristetes und widerrufbares **Delegationsrecord** ("Vendor X delegiert
Publikationsrecht für Namespace Z an Trusted Provider Y, gültig von–bis"). Governance-Vorbild: der
bereits erfolgreich durchlaufene RVISC-Prozess (siehe Meeting-Minutes 2026-04-29).

## Offene Fragen

- Widerrufs-/Ablaufmechanismus für Delegationsrecords (Wiederverwendung der Signatur-
  Gültigkeitslogik aus Requirement 19?).
- Missbrauchsschutz: wie wird verhindert, dass sich jemand fälschlich als Delegierter eines Vendors
  ausgibt?
- Governance: wer registriert/prüft Delegationen — TP-seitig, TC-seitig, oder ein Registry-Ansatz
  analog RVISC?

## TODO

Konkreten Spec-Text sowie neue Mandatory Tests für die Signaturkette ausformulieren (siehe README,
Abschnitt "Offene Punkte / Nicht vergessen").
