import csv
import unittest
from collections import defaultdict

from problem_01.recommender import initialize, top_5_product

import logging
import sys

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)

USER_PREFERENCE_FILE = "test_user_preference.txt"
PRODUCT_SCORE_FILE = "test_product_score.txt"


def read_tsv(input_file):
    colls = defaultdict(list)
    with open(input_file, 'r') as f:
        reader = csv.DictReader(f, dialect='excel-tab')
        for row in reader:
            for (k, v) in row.items():
                colls[k].append(v)
        f.close()
    return colls


class RecommenderTestCase(unittest.TestCase):
    def setUp(self):
        self.user_preference = read_tsv(USER_PREFERENCE_FILE)
        self.product_score = read_tsv(PRODUCT_SCORE_FILE)
        self.calculated_score = None

    def test_initialize(self):
        self.calculated_score = initialize(USER_PREFERENCE_FILE, PRODUCT_SCORE_FILE)
        self.assertEqual(self.calculated_score, [['12341', '2123', 240], ['12341', '2939', 480]])

    def test_top_five(self):
        top_five = top_5_product('12341')
        logger.info(top_five)
        self.assertListEqual(top_five, ['2939', '2123'])


if __name__ == '__main__':
    unittest.main()
