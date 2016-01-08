from django.test import TestCase
from wmata_realtime_snapshot.realtime import RealTime

class RealTimeTests(TestCase):

    def setUp(self):
        self.rt = RealTime()

    def test_json_all(self):
        result = self.rt.get_realtime_json(['All'])
        self.assertEqual(len(result['Trains']), 462)
        # TODO not really testing the integrity of the data

    def test_json_single(self):
        result = self.rt.get_realtime_json(['B01'])
        self.assertEqual(len(result['Trains']), 6)
        for train in result['Trains']:
            self.assertTrue(train['LocationCode'] == 'B01')

    def test_json_multiple(self):
        locations = ['B01', 'C02', 'A07']
        result = self.rt.get_realtime_json(locations)
        self.assertEqual(len(result['Trains']), 18)
        for train in result['Trains']:
            self.assertTrue(train['LocationCode'] in locations)

    def test_xml_all(self):
        result = self.rt.get_realtime_xml(['All'])
        self.assertEqual(len(result[0]), 462)
        # TODO not really testing the integrity of the data

    def test_xml_single(self):
        result = self.rt.get_realtime_xml(['B01'])
        self.assertEqual(len(result[0]), 6)
        for train in result[0]:
            code = train.find('{http://www.wmata.com}LocationCode')
            self.assertTrue(code.text == 'B01')

    def test_xml_multiple(self):
        locations = ['B01', 'C02', 'A07']
        result = self.rt.get_realtime_xml(locations)
        self.assertEqual(len(result[0]), 18)
        for train in result[0]:
            code = train.find('{http://www.wmata.com}LocationCode')
            self.assertTrue(code.text in locations)

