from unittest import TestCase
from attitude import Attitude

class Tests(TestCase):

    def test_statement_is_happy(self):
        happy_english = "It is so good to see you again."
        attitude = Attitude(happy_english)

        self.assertTrue(attitude.get_sentiment() == "happy")

    def test_statement_is_angry(self):
        angry_english = "Would you stop that! I hate how you always make " \
                        "those stupid sounds when you are thinking."
        attitude = Attitude(angry_english)

        self.assertTrue(attitude.get_sentiment() == "angry")

    def test_statement_is_angry_spanish(self):
        angry_spanish = "Podrias dejar eso! No me gusta lo que siempre haces " \
                        "esos sonidos estupidos cuando usted esta pensando."
        attitude = Attitude(angry_spanish)

        self.assertTrue(attitude.get_sentiment() == "angry")
