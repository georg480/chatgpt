```
+----------------+              +----------------+
|   TestFunctions|              |    unittest    |
+----------------+              +----------------+
| test_pruefe_py_+---------------> mock_subproces |
|   gebaut()     |              | s_call.assert_ |
|                |              | has_calls()    |
+----------------+              +----------------+
        |                                   ^
        |                                   |
        |                                   |
+----------------+              +----------------+
|     TestMyFunc  |              |    builtins    |
|      tions     |              +----------------+
+----------------+              | input.assert_  |
| test_eingabe() |<--------------| called_once_wi |
| test_eingabe_l |              | th(anzeige)    |
| eer()          |              +----------------+
+----------------+                      ^
        |                               |
        |                               |
        |                               |
+----------------+              +----------------+
|   models.functi|              |     call       |
|      ons       |              +----------------+
+----------------+

