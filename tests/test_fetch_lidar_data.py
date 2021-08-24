import unittest
import sys
sys.path.append("..")
from scripts.region_selector import dataset_path
from scripts.region_selector import SelectName

class Test_region_selector(unittest.TestCase):

    def test_SelectName(self):
        self.assertEqual(print(SelectName("IA_FullState")), "IA_FullState")

    def test_dataset_path(self):
        self.assertEqual(print(dataset_path("IA_FullState"), "https://s3-us-west-2.amazonaws.com/usgs-lidar-public/IA_FullState/ept.json"))


if(__name__ == '__main__'):
    unittest.main()
