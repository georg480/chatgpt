```plantuml
@startuml
class dateien {
  - datei_namen: str
  + schreibe_protokol(datei_namen: str, inhalt_einfuegen: str) -> None
  + lese_datei(datei_namen: str) -> str
  + schreibe_md(datei_namen: str, datei_inhalt: str) -> None
  + schreibe_datei(datei_namen: str, inhalt_einfuegen: str) -> None
  + lese_gesuchte_dateinamen(suchfilter: str) -> List[str]
  + aendere_datei_pfard(datei: str) -> str
  + gebe_nur_dateinamen(datei_namen: str) -> str
}
@enduml

