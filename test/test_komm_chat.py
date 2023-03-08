import unittest

from gpt3 import gpt3


class TestGPT3(unittest.TestCase):
    def setUp(self):
        self.prompt = """Human: Hey, how are you doing?\nAI: I'm good! What would you like to chat about?\nHuman:"""

    def test_komm_chat(self):
        # Testet ob die Funktion komm_chat das richtige Ergebnis gibt
        expected_answer, expected_prompt = gpt3(
            self.prompt,
            temperature=0.9,
            frequency_penalty=1,
            presence_penalty=1,
            start_text="\nAI:",
            restart_text="\nHuman: ",
            stop_seq=["\nHuman:", "\n"],
        )
        self.assertEqual(expected_answer, answer)
        self.assertEqual(expected_prompt, promp)
