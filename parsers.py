

class ParserTXT:

    def __init__(self, path, sep):
        self.path = path
        self.sep = sep

    def parse(self):
        data = []
        row_number = 0
        with open(f'{self.path}', 'w') as file:
            for row in file:

                if row_number == 0:
                    data.append([row.split(',')])

                else:

                    data