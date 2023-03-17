```plantuml
@startuml
class dateien {
    -schreibe_protokol(datei_namen, inhalt_einfuegen): void
    +lese_datei(datei_namen): str
    +schreibe_datei(datei_namen, inhalt_einfuegen): void
}
@enduml

