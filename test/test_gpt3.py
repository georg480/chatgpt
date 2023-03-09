# import os
# import unittest
#
# import dotenv
# import openai
#
#
# class TestGPT3(unittest.TestCase):
#     def test_gpt3(self):
#         dotenv.load_dotenv()
#         openai.api_key = os.getenv("OPENAI_API_KEY")
#         response_length = 200
#         temperature = 0.7
#         top_p = 1
#         frequency_penalty = 0
#         presence_penalty = 0
#         start_text = ""
#         restart_text = ""
#         stop_seq = []
#
#         result, _ = gpt3(
#             "Ich möchte mehr über",
#             response_length=response_length,
#             temperature=temperature,
#             top_p=top_p,
#             frequency_penalty=frequency_penalty,
#             presence_penalty=presence_penalty,
#             start_text=start_text,
#             restart_text=restart_text,
#             stop_seq=stop_seq,
#         )
#
#         self.assertLessEqual(len(result), response_length)
#         self.assertGreaterEqual(temperature, 0.7)
#         self.assertEqual(top_p, 1)
#         self.assertEqual(frequency_penalty, 0)
#         self.assertEqual(presence_penalty, 0)
#         self.assertNotIn(stop_seq, result)
#
#
# if __name__ == "__main__":
#     unittest.main
