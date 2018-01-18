import random


def generate_ages(output_file, size):
    """
    generate ages dataset with value in range 0 to 150
    :param output_file: file path for generated dataset
    :param size: number of data to generate
    """
    with open(output_file, 'w') as f:
        f.truncate()
        for i in range(0, size):
            f.write('{}\n'.format(random.randint(0, 150)))
        f.close()


if __name__ == '__main__':
    generate_ages("../age.txt", 100000000)
