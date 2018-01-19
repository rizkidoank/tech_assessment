import csv
import random
from collections import defaultdict
from datetime import datetime, timedelta

PRODUCT_SCORE_FILE = '../product_score.txt'
USERS_ID_FILE = '../users_id.txt'
USER_PREFERENCE_FILE = '../user_preference.txt'


def generate_product_score(output_file, size):
    """
    generate product scores
    :param output_file: file path for output
    :param size: number of row (number of product-scores)
    """
    with open(output_file, 'w') as f:
        f.truncate()
        fields = ['pid', 'score']
        writer = csv.DictWriter(f, dialect='excel-tab', fieldnames=fields)
        writer.writeheader()
        for i in range(0, size):
            writer.writerow({
                'pid': 2000 + i,
                'score': random.randint(0, 1000)
            })
        f.close()


def generate_users(output_file, size):
    """
    method to generate users id
    :param output_file: file path for output
    :param size: number of row for users id (num of users)
    """
    with open(output_file, 'w') as f:
        f.truncate()
        fields = ['uid']
        writer = csv.DictWriter(f, dialect='excel-tab', fieldnames=fields)
        writer.writeheader()
        for i in range(0, size):
            writer.writerow({'uid': 1000 + i})
        f.close()


def read_tsv(input_file):
    """
    function to read tsv file
    :param input_file: file path of tsv file
    :return: dictionary of dataset
    """
    colls = defaultdict(list)
    with open(input_file, 'r') as f:
        reader = csv.DictReader(f, dialect='excel-tab')
        for row in reader:
            for (k, v) in row.items():
                colls[k].append(v)
        f.close()
    return colls


def random_timestamp_days_behind(start, days):
    """
    timestamp generator, get random timestamp in range(start-days, start)
    :param start: start of days, example : datetime.now()
    :param days: number of days before, example: 30 to get 30 days behind
    :return: random timestamp between (start-days, start)
    """
    start = start
    random_date = start + timedelta(days=days) * random.random()
    return int(random_date.timestamp())


def generate_user_preference(
        output_file,
        product_score_file,
        users_id_file,
        size):
    """
    generate user preference data
    :param output_file: file path for user preference
    :param product_score_file: file path of product score, to get product score
    :param users_id_file: file path of users id, to get user id
    :param size: number of row for user preference
    """
    product_score = read_tsv(product_score_file)
    users_ids = read_tsv(users_id_file)

    with open(output_file, 'w') as f:
        f.truncate()
        fields = ['uid', 'pid', 'score_double', 'timestamp']
        writer = csv.DictWriter(f, dialect='excel-tab', fieldnames=fields)
        writer.writeheader()
        now = datetime.now()
        tmp = {x: [] for x in users_ids['uid']}
        for i in range(0, size):
            flag = False
            uid = random.choice(users_ids['uid'])
            pid = None
            while not flag:
                pid = random.choice(product_score['pid'])
                if pid not in tmp[uid]:
                    tmp[uid].append(pid)
                    flag = True
            uid_pid = [uid, pid]
            writer.writerow({
                'uid': uid_pid[0],
                'pid': uid_pid[1],
                'score_double': float("{0:.3f}".format(random.uniform(-1, 1))),
                'timestamp': random_timestamp_days_behind(now, 30)
            })
        f.close()


if __name__ == '__main__':
    generate_product_score(PRODUCT_SCORE_FILE, 100)
    generate_users(USERS_ID_FILE, 20)
    generate_user_preference(
        USER_PREFERENCE_FILE,
        PRODUCT_SCORE_FILE,
        USERS_ID_FILE,
        1000)
