# import unittest
#
# from gpt3 import gpt3
#
#
# class KommChatTest(unittest.TestCase):
#     def test_komm_chat(self):
#         prompt = """Human: Erkläre alles auf deutsch\nAI: \nHuman:"""
#         expected = "GPT-3:Ich versuche mein Bestes, um alles auf Deutsch zu erklären."
#         answer, prompt = gpt3(
#             prompt,
#             temperature=0.9,
#             frequency_penalty=1,
#             presence_penalty=1,
#             start_text="\nAI:",
#             restart_text="\nHuman: ",
#             stop_seq=["\nHuman:", "\n"],
#         )
#         self.assertEqual(answer, expected)
