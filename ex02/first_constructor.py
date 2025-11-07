import sys
import os

class Research:

    def __init__(self, path):
        self.path = path


    def file_reader(self):  
        lines = []
        if not os.path.exists(self.path):
            raise Exception("file not found")

        with open(self.path, "r") as file:
            for line in file:
                lines.append(line.strip())

        if not lines:
            raise Exception("file pustoy")

        header = lines[0].split(",")
        if len(header) != 2:
            raise Exception("piska")

        for line in lines[1:]:
            if line not in ["0,1", "1,0"]:
                raise Exception("nepravilnye dannye")
        return lines
            

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
        print("Usage: python first_method.py <path_to_csv>")
        sys.exit(1)

    path = sys.argv[1]
    research = Research(path)
    lines = research.file_reader()

    for line in lines:
        print(line)

    

