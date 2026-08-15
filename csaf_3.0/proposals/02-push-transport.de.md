# Proposal 2 — Push-Transport (WebSub-Erweiterung)

*[Read this page in English](02-push-transport.md)* — dies ist eine wortgetreue, vollständige
Übersetzung des englischen Originaldokuments. Im Zweifelsfall ist die englische Fassung maßgeblich.

**Status:** Skizze, noch kein Spec-Textvorschlag. Siehe [../README.de.md](../README.de.md) für
Motivation und Einordnung gegenüber den anderen drei Proposals.

**Abhängigkeiten:** Baut auf keinem der anderen Proposals zwingend auf, ist aber ohne P3 nur für
öffentliche (TLP:CLEAR/GREEN) Kanäle sinnvoll nutzbar. Liefert idealerweise das P1-Event als Payload.

## Ziel

Optionale, zusätzliche Push-Fähigkeit für Trusted Provider, ohne den bestehenden Pull-Mechanismus
(ROLIE-Feed, Requirements 15–17) zu ersetzen.

## Mechanismus (Kurzfassung)

Basiert auf [WebSub](https://www.w3.org/TR/websub/) (W3C Recommendation, 2018):

1. **Topic** = bestehender ROLIE-Category-Feed pro Produkt (Requirement 17).
2. **Hub** = neue, optionale Fähigkeit des Trusted Providers (oder eines von ihm benannten
   Drittanbieter-Hubs).
3. Subscriber abonniert per Standard-WebSub-Handshake (inkl. `hub.challenge`-Verifikation gegen
   Missbrauch).
4. Bei neuer/geänderter Veröffentlichung: Hub benachrichtigt Subscriber — Payload = P1-Event statt
   nur "geh nachgucken".

## Verpflichtende Sicherheitsnetz-Anforderung

Der Pull-Mechanismus bleibt in jedem Fall die maßgebliche Quelle. Subscriber MÜSSEN in der Lage sein,
nach einer erkannten Lücke (eigener Timestamp vs. Feed/`changes.csv`) zu rekonziliieren, ohne auf den
Hub angewiesen zu sein (siehe Diskussion im README, Abschnitt "Offene Punkte").

## Offene Fragen

- Retention-Fenster für Feed/`changes.csv` als Rekonziliationsbasis (aktuell nicht spezifiziert).
- Lease-/Renewal-Handling für langlebige Kunden-Subscriptions.
- Betrieb des Hubs durch Dritte (Analogie Superfeedr) — welche Anforderungen gelten dann?

## TODO

Konkreten Spec-Text (neues Requirement in Abschnitt 7.1, neue Rolle oder Zusatz zu "CSAF Trusted
Provider" in 7.2) ausformulieren.
