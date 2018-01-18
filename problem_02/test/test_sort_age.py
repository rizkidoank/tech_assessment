import unittest

from problem_02.test.generator import generate_ages
from problem_02.sort_age import count_ages, sort_ages

INPUT_FILE = "test_age.txt"
OUTPUT_FILE = "test_sorted_age.txt"
DATA_SIZE = 100000


def read_data(file_path):
    """
    simple dataset reader, open dataset, assign to list, return result (list)
    :param file_path: dataset file path
    :return: list of ages in dataset
    """
    f = open(file_path, 'r')
    tmp = []
    for line in f:
        tmp.append(int(line))
    f.close()
    return tmp


class SortTestCase(unittest.TestCase):
    def setUp(self):
        # generate dataset before tests
        generate_ages(INPUT_FILE, DATA_SIZE)

    def test_count(self):
        """
        assert : total of counted ages should be equal to DATA_SIZE
        """
        ages = count_ages(INPUT_FILE)
        count = 0
        for k, v in ages.items():
            count += v
        self.assertEqual(count, DATA_SIZE)

    def test_sort(self):
        """
        assert : count sort output should be equal to sorted data in INPUT_FILE
        """
        sort_ages(INPUT_FILE, OUTPUT_FILE)

        input_sorted = sorted(read_data(INPUT_FILE))
        output = read_data(OUTPUT_FILE)

        self.assertListEqual(output, input_sorted)


if __name__ == '__main__':
    unittest.main()
