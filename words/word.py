import re


class Word:

    """ Simple class to build concordance from provided text.
    """

    def __init__(self, data):
        self.data = data

    def sentences(self, split_words=True):
        """ Represent data as list of sentences.
        """

        sentence_sep = re.compile(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s")
        sentences = [s.strip()
                     for s in re.split(sentence_sep, self.data.strip())]

        if split_words:
            word_sep = re.compile(r"\W?\s+")
            sentences = [re.split(word_sep, sentence)
                         for sentence in sentences]

        return sentences

    def concordance(self):
        """ Builds concordance from provided text.
        """

        concordance = {}
        for i, sentence in enumerate(self.sentences(), start=1):
            sentence = [w.lower() for w in sentence]
            for word in sentence:
                count = sentence.count(word)
                if word in concordance:
                    if i in concordance[word][1]:
                        continue
                    else:
                        concordance[word] = [
                            concordance[word][0] + count,
                            concordance[word][1] + [i]*count]
                else:
                    concordance[word] = [count, [i]*count]

        concordance = list(concordance.items())
        concordance.sort()
        return concordance
