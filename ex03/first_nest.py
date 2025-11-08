import sys
import os

class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self, has_header=True):
        if not os.path.exists(self.path):
            raise Exception("file not found")

        with open(self.path, "r") as file:
            lines = [line.strip() for line in file if line.strip()]

        if not lines:
            raise Exception("file is empty")

      
        if has_header:
            lines = lines[1:]

        data = []
        for line in lines:
            parts = line.split(",")
            if parts not in [["0", "1"], ["1", "0"]]:
                raise Exception("invalid data format")
            data.append([int(parts[0]), int(parts[1])])
        return data

    class Calculations:
        @staticmethod
        def counts(data):
            heads = sum(1 for x in data if x == [1, 0])
            tails = sum(1 for x in data if x == [0, 1])
            return (heads, tails)

        @staticmethod
        def fractions(heads, tails):
            total = heads + tails
            return (heads / total * 100 , tails / total * 100)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python first_nest.py <path_to_csv>")
        sys.exit(1)

    path = sys.argv[1]
    research = Research(path)

    data = research.file_reader(has_header=True)
    print(data)

    calc = research.Calculations()
    heads, tails = calc.counts(data)
    print(heads, tails)

    heads_perc, tails_perc = calc.fractions(heads, tails)
    print(heads_perc, tails_perc)
