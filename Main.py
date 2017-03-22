from File import File
import TestFile
from TestFile import TestFile
import unittest
import glob

def main():
    g = open('wynik.txt','w')
    d = File()
    for filename in glob.glob("./Logs/*.log"):
        d.set_name(filename)
        print(g,  "File:", filename, "content:", d.word_count_all(), "words")
        print(g, "I found", d.grep("PrChecker.Downs"))
    g.close()


if __name__ == '__main__':
    unittest.main()
    main()
