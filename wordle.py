from collections import defaultdict

f=open('/home/shubham/Downloads/words.txt')
words = [word.lower() for word in f.read().split("\n") if len(word)==5]

class Wordle():
    disjoint_alphabets = []
    wrong_places_alphabets = defaultdict(list)
    right_places_alphabets = {}
    def update(self, word, colors):
        word = word.lower()
        assert(len(word)==5)
        assert(len(colors)==5)
        for i in range(5):
            if colors[i] == "black" or colors[i] == "b":
                self.disjoint_alphabets.append(word[i])
            elif colors[i] == "green" or colors[i] == "g":
                self.right_places_alphabets[i] = word[i]
            elif colors[i] == "yellow" or colors[i] == "y":
                self.wrong_places_alphabets[i].append(word[i])
            else:
                assert(0)
    def get_choices(self):
        def satisfies_wrong_places(word):
            for i in self.wrong_places_alphabets.keys():
                if word[i] in self.wrong_places_alphabets[i]:
                    return False
                # wrong places alphabets must be *somewhere* in the word 
                if not set([item for sublist in self.wrong_places_alphabets.values() for item in sublist]).issubset(word):
                    return False
            return True
        def satisfies_right_places(word):
            for i in self.right_places_alphabets.keys():
                if word[i] != self.right_places_alphabets[i]:
                    return False
            return True
        ret_choices = []
        for word in words:
            if set(word).isdisjoint(set(self.disjoint_alphabets)) and satisfies_wrong_places(word) and satisfies_right_places(word):
                ret_choices.append(word)
        return ret_choices

