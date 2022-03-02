class Word :
    def __init__(self,wort):
        self.word = wort
        self.wortliste = []
        for i in range(len(wort)):
            self.wortliste.append("_")
        self.errors = 0
        self.word_guess = []
    def testword(self,buchstabe):
        if buchstabe in self.word:
            self.word_guess.append(buchstabe)
            for i in range(len(self.word)):
                if self.word[i] == buchstabe:
                    self.wortliste.insert(i,buchstabe)
            return True
        else:
            self.errors += 1
            return False
    def getWort(self):
        return self.wortliste
    def geterros(self):
        return self.errors
    def getWordGuess(self):
        return self.word_guess
    def delob(self):
        if not "_" in self.wortliste:
            del[self]
            return True

obj = Word("hallo")
print (obj.getWordGuess())
print (obj.getWort())
print (obj.geterros())
print (obj.testword("l"))
print (obj.getWordGuess())
print (obj.getWort())
print (obj.geterros())
