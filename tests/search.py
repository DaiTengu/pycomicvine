import pycomicvine
import unittest

api_key = "476302e62d7e8f8f140182e36aebff2fe935514b"

class TestSearch(unittest.TestCase):
    def test_search_resource_type(self):
        search = pycomicvine.Search(
                resources="volume", 
                query="Angel"
            )
        for v in search:
            self.assertIsInstance(v, pycomicvine.Volume)

    def test_search_id(self):
        search = pycomicvine.Search(
                query="The Walking Dead",
                field_list=["id"]
            )
        self.assertNotEqual(len(search),0)
        self.assertEqual(18166, [s.id for s in search])

