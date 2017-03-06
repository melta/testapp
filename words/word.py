import re

SENT_SEP = r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s"
WORD_REGX = r"((?:[A-Za-z]\.)+|\w+(?:[-']\w+)*)|'|[-.(]+|\S\w*"


class Word:
    """ Represents word in concordance.

    Simple class that holds word information. Used by `Conconrdance`
    to help calcute the word frequencies, and occurrences in sentence.
    """

    def __init__(self, data):
        self.data = data
        self.frequency = 0
        self.sentences = ()

    def __str__(self):
        """ Word string representation.

        Example: "application {1:1,2}"
        """
        return "%s {%s:%s}" % (self.data, self.frequency,
                               ",".join(map(str, self.sentences)))


class Concordance:

    """ Concordance class.

    Processes data input and builds concordance from it.
    To get concordance call `concordance` method.
    """

    def __init__(self, data):
        self.data = self.prepare(data)

    def prepare(self, data):
        """ Strip spaces. """

        return data.strip()

    def get_sentences(self):
        """ Represents data as list of sentences. """

        return [s.lower().strip()
                for s in re.split(re.compile(SENT_SEP), self.data)]

    def get_words(self, str_):
        """ Splists provided string to words. """

        return [w.strip()
                for w in re.findall(re.compile(WORD_REGX), str_) if w]

    def concordance(self):
        """ Builds concordance.
        """

        concordance = {}
        for i, sentence in enumerate(self.get_sentences(), start=1):
            words = self.get_words(sentence)
            for word in words:
                count = words.count(word)
                if word in concordance:
                    word = concordance[word]
                    if i not in word.sentences:
                        word.frequency += count
                        word.sentences = tuple(
                            list(word.sentences) + [i]*count)
                else:
                    concordance[word] = word = Word(word)
                    word.frequency = count
                    word.sentences = tuple([i]*count)

        concordance = list(concordance.items())
        concordance.sort()
        return concordance
