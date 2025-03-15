import unittest
from modules.weather_events.weather_fetcher import test_module as test_weather
from modules.weather_events.events_fetcher import test_module as test_events

class TestWeatherEvents(unittest.TestCase):
    def test_weather(self):
        self.assertIn("天気", test_weather())
    def test_events(self):
        self.assertIn("イベント", test_events())

if __name__ == "__main__":
    unittest.main()
