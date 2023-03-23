```mermaid
class dateien {
    -schreibe_protokol(datei_namen, inhalt_einfuegen)
    +lese_datei(datei_namen)
    -schreibe_md(datei_namen, datei_inhalt)
    +schreibe_datei(datei_namen, inhalt_einfuegen)
    +lese_gesuchte_dateinamen(suchfilter)
    +aendere_datei_pfard(datei)
    +gebe_nur_dateinamen(datei_namen)
}

