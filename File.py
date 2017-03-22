class File:
    def _init_(self, filename):
        self.filename = filename

    def word_count_all(self):
        wordcount = 0
        with open(self.filename) as f:
            for word in f.read().split():
                wordcount = wordcount + 1
            return wordcount

    def set_name(self, filename):
        self.filename = filename

    def grep(self, word):
        with open(self.filename) as f:
            for line in f:
                if word in line:
                    next(f)
                    return line
