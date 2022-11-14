from iterator import Iterator


def main():

    i = Iterator("annotation.csv", "rose")
    for val in i:
        print(val)

    i = Iterator("annotation.csv", "tulip")
    for val in i:
        print(val)

    print('program finished')


if __name__ == '__main__':
    main()
