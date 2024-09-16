
from unittest import TestCase
from weather_server import get_city_weather

class ModeTest(TestCase):

    def setUp(self) -> None:
        pass

    def test_get_city_weather(self):
        w1 = get_city_weather('Tehran') 
        self.assertTupleEqual(w1,(26.730000000000018, 26.110000000000014, '2024-09-16 18:25:48'))
        # self.assertEqual(w1[1],26.110000000000014)

