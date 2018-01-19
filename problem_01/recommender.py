import datetime
import csv
import operator

USER_PREFERENCE_FILE = 'user_preference.txt'
PRODUCT_SCORE_FILE = 'product_score.txt'
calculated_scores = []


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
    final_score = []
    for i in range(0, len(preferences)):
        row = preferences[i]
        user_id = row[0]
        product_id = row[1]
        score = float(row[2])
        time_stamp = int(row[3])
        product_score = int(get_score_by_id(product_score_file, product_id))

        day_difference = round(abs((datetime.datetime.now().timestamp() - time_stamp) / 24 / 3600))
        effective_score = round(score * (0.95 ** day_difference), 3)

        calculated_score = round(product_score * effective_score + product_score)

        final_score.append([user_id, product_id, calculated_score])
    global calculated_scores
    calculated_scores = final_score
    print("DONE")


def top_5_product(uid):
    global calculated_scores
    uids_scores = []
    for row in range(len(calculated_scores)):
        if calculated_scores[row][0] == uid:
            uids_scores.append(calculated_scores[row])

    uids_scores = sorted(uids_scores, key=operator.itemgetter(2), reverse=True)
    for product in uids_scores[0:5]:
        print(product[1])


if __name__ == '__main__':
    product_score = read_tsv(PRODUCT_SCORE_FILE)
    user_preference = read_tsv(USER_PREFERENCE_FILE)

    initialize(USER_PREFERENCE_FILE, PRODUCT_SCORE_FILE)
    top_5_product('1002')
