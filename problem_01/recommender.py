import argparse
import csv
from operator import itemgetter
import pickle
from datetime import datetime

USER_PREFERENCE_FILE = 'user_preference.txt'
PRODUCT_SCORE_FILE = 'product_score.txt'


def read_tsv(input_file):
    tmp = []
    with open(input_file, 'r') as f:
        reader = csv.reader(f, dialect='excel-tab')
        next(reader)
        for row in reader:
            tmp.append(row)
        f.close()
    return tmp


def get_score_by_id(product_score_file, pid):
    products = read_tsv(product_score_file)
    for row in products:
        if row[0] == pid:
            return row[1]


def initialize(user_preference_file, product_score_file):
    preferences = read_tsv(user_preference_file)
    scores = []

    for i in range(0, len(preferences)):
        row = preferences[i]
        user_id = row[0]
        product_id = row[1]
        score = float(row[2])
        time_stamp = int(row[3])

        product_score = int(get_score_by_id(product_score_file, product_id))
        day_difference = abs((datetime.now() - datetime.fromtimestamp(time_stamp)).days)

        effective_score = round(score * (0.95 ** day_difference), 3)
        calc_score = round(product_score * effective_score + product_score)

        scores.append([user_id, product_id, calc_score])
    with open('tmp.dat', 'wb') as f:
        f.flush()
        pickle.dump(scores, f)
        f.close()

    return scores


def top_5_product(uid):
    uids_scores = []
    with open('tmp.dat', 'rb') as f:
        calculated_scores = pickle.load(f)
        f.close()

    for row in range(len(calculated_scores)):
        if calculated_scores[row][0] == uid:
            uids_scores.append(calculated_scores[row])
    uids_scores = sorted(uids_scores, key=itemgetter(2), reverse=True)[0:5]
    return [x[1] for x in uids_scores]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--initialize', action='store_true')
    parser.add_argument('--recommend-products')
    parser.add_argument('--read-tsv')

    args = parser.parse_args()
    if args.initialize:
        initialize(USER_PREFERENCE_FILE, PRODUCT_SCORE_FILE)
    elif args.recommend_products:
        try:
            for product in top_5_product(args.recommend_products):
                print(product)
        except:
            exit(1)
    elif args.read_tsv:
        data = read_tsv(args.read_tsv)
        for row in data:
            print(row)
    else:
        parser.print_help()
