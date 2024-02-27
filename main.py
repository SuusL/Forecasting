from parsers import ParserTXT


def main():
    parser = ParserTXT('./data.txt', ',')
    parser.parse()
    print(parser.data[1])


if __name__ == "__main__":
    main()
