def count_ages(input_file):
    # initialize 0 valued dictionary with keys 0 to 150
    # assuming 150 is max value for oldest age in the world
    ages = {x: 0 for x in range(0, 151)}
    try:
        f = open(input_file, 'r')
        for line in f:
            age = int(line)
            ages[age] += 1
        f.close()
    except Exception as e:
        print(e)

    # cleanup all 0 valued occurrences if any
    ages = {k: v for k, v in ages.items() if v != 0}

    return ages


def sort_ages(input_file, output_file):
    # count occurrences of ages from input file
    ages = count_ages(input_file)

    # loop over the counted ages and write to output file
    try:
        f = open(output_file, 'w')
        for k, v in ages.items():
            f.truncate()
            for i in range(v):
                f.write('{}\n'.format(k))
        f.close()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    sort_ages('age.txt', 'sorted_age.txt')
