```
+----------------+            +-------------+
| TestFunctions  |            | builtins    |
+----------------+            +-------------+
| - test_pruefe_ |            | - input()   |
|   py_gebaut()  |            +-------------+
| - test_eingabe |
|   ()           |
| - test_eingabe |
|   _leer()      |
+----------------+
         |
         |
         v
+----------------+            +----------------+
| subprocess     |            | models.functions|
+----------------+            +----------------+
| - call()       |            | - eingabe()     |
+----------------+            | - pruefe_py_ge- |
                               |   baut()        |
                               +----------------+

