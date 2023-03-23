```
         +----------------+                    +---------+
         | TestKommChat   |                    |  patch  |
         +----------------+                    +---------+
         | test_komm_chat |     calls           |  input  |
         +----------------+                    +---------+
                 |                                   |
        +--------+--------+                  +-------+--------+
        |                 |                  |                |
+----------------+ +----------------+  +----------------+ +-------------+
|   mock_print   | |   patch_print  |  |  mock_input    | |   patch_input|
+----------------+ +----------------+  +----------------+ +-------------+
| assert_any_call| | assert_any_call|  | assert_called_ | |   side_effect|
+----------------+ +----------------+  | with('Was ist  | +-------------+
                                        | das Wetter    |
                                        | heute?', 'Was|
                                        | ist deine     |
                                        | Lieblingsfarbe|
                                        | ?')           |
                                        +---------------+

