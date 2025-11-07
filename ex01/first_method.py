class Research:

    def file_reader(self):
        lines = []
        with open("data.csv", "r") as file:
            for line in file:
                lines.append(line.strip())
        return lines

if __name__ == "__main__":
    research = Research()
    liens = research.file_reader()

    for line in liens:
        print(line)
