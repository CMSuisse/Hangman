class Word :
    def __init__(self, wort: str) -> None:
        self.word = wort.lower()
        self.word.replace("ä", "ae")
        self.word.replace("ö", "oe")
        self.word.replace("ü", "ue")
        self.wortliste = []
        for i in range(len(wort)):
            self.wortliste.append("_")
        self.errors = 0
        self.word_guess = []

    def testword(self, buchstabe: str) -> bool:
        if buchstabe in self.word:
            for i in range(len(self.word)):
                if self.word[i] == buchstabe:
                    self.wortliste[i] = buchstabe
            return True
        else:
            if buchstabe not in self.word_guess:
                self.word_guess.append(buchstabe)
            self.errors += 1
            return False

    def getWort(self) -> list:
        return self.wortliste

    def geterrors(self) -> int:
        return self.errors

    def getLetterGuess(self) -> list:
        return self.word_guess

    def delob(self) -> bool:
        if not "_" in self.wortliste:
            del[self]
            return True
        return False