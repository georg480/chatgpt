flowchart LR
start[Start] --> a
a[Menü anzeigen] --> b{Menüauswahl}
b -- 1 --> c[Automatischer Test]
c --> d[Tastatureingabe]
b -- 2 --> e[Manueller Test]
e --> d[Tastatureingabe]
b -- 3 --> f[Exit]
f --> end[Ende]
d -- "Auswahl ungültig" --> a
