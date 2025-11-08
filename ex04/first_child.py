import sys
from random import randint

class Research:
    def __init__(self, path):
        self.path = path

    def file_reader(self, has_header=True):
        try:

            with open(self.path, "r") as file:
                lines = [line.strip() for line in file if line.strip()]

        except FileNotFoundError:
            raise Exception("file not found")

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
        
        def __init__(self, data):
            self.data = data

        def counts(self):
            heads = sum(1 for x in data if x == [1, 0])
            tails = sum(1 for x in data if x == [0, 1])
            return (heads, tails)

        
        def fractions(self, heads, tails):
            total = heads + tails
            return (heads / total * 100 , tails / total * 100)

class Analytics(Research.Calculations):

    def predict_random(self, num_predictions):
        predictions = []
        for _ in range(num_predictions):
            flip = randint(0, 1)
            if flip == 1:
                predictions.append([1, 0])
            else:
                predictions.append([0, 1])
        return predictions  

    def predict_last(self):
        return self.data[-1]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("dolbaeb")
        sys.exit(1)

    path = sys.argv[1]
    research = Research(path)

    data = research.file_reader(has_header=True)
    print(data)

    analytics = Analytics(data)
    heads, tails = analytics.counts()
    print(heads, tails)

    heads_perc, tails_perc = analytics.fractions(heads, tails)
    print(heads_perc, tails_perc)

    random_preds = analytics.predict_random(3)
    print(random_preds)

    last_pred = analytics.predict_last()
    print(last_pred)


    


    

