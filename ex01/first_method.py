class Research:
    def file_reader():
        lines = []
        with open("data.csv", "r") as file:
            for line in file:
                lines.append(line.strip())
        return lines

if __name__ == "__main__":
    for line in Research.file_reader():
        print(line)
    

