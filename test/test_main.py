# import unittest
# import os
#
# from komm_chat import komm_chat
# from models.dateien import lese_datei, schreibe_datei
# from openai_com import chat, erzeuge_unittest
#
# MODEL = "text-davinci-003"
#
#
# class TestKommChat(unittest.TestCase):
#     def test_komm_chat(self):
#         self.assertTrue(komm_chat())
#
#     def test_lese_datei(self):
#         test_inhalt = lese_datei("englischer_text.txt")
#         self.assertIsNotNone(test_inhalt)
#
#     def test_schreibe_datei(self):
#         test_inhalt = lese_datei("englischer_text.txt") + "\nNeuer Inhalt"
#         schreibe_datei("deutscher_text.txt", test_inhalt)
#         self.assertEqual(lese_datei("deutscher_text.txt"), test_inhalt)
#
#     def test_chat(self):
#         anweisung = "Erkläre was der Code macht!"
#         antwort = chat(anweisung, MODEL, 1024)
#         self.assertIsNotNone(antwort)
#
#     def test_erzeuge_unittest(self):
#         skript_name = "test_skript.py"
#         test_name = erzeuge_unittest(skript_name, MODEL)
#         self.assertTrue(os.path.exists(test_name))
#
#
