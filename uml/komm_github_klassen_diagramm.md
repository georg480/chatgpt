```
+------------------+                +------------------+
|  subprocess      |                |     GitCommit    |
+------------------+                +------------------+
|  call(args)      |                |  commit_message  |
|  check_output()  |                |  author_info     |
+------------------+                +------------------+
        |                                        |
        |                                        |
        |                uses                    |
        |                                        |
        |                                        |
+----------------+                      +-------------------+
|   komm_github  |                      | commit_template   |
+----------------+                      +-------------------+
|  git_commit()  |                      |                   |
|  git_push()    |                      |                   |
+----------------+                      +-------------------+

