from dictionary import La
import sys

class wordlist:
    def __init__(self):
        self.words=La
    def remove(self, letter):
        self.words=[word for word in self.words if letter not in word]
    def fix(self, letter, place):
        self.words=[word for word in self.words if letter == word[place]]
    def sweep(self, letter, place):
        self.words=[word for word in self.words if letter != word[place] and letter in word]
    def choose(self):
            m = 1000
            r = ""
            x = []
            i = 0
            for word in self.words:
                i +=1
                if i % 1000 == 0:
                    print(i)
                b = [e for e in self.words if all(ch not in e for ch in [c for c in word])]
                if len(b) < m:
                    m = len(b)
                    r=word
            return r


def check_result(word, goal):
    resp = ''
    for i in range(len(goal)):
        if word[i] == goal[i]:
            resp += "2"
        elif word[i] in goal:
            resp += "1"
        else:
            resp += "0"
    return resp


def play(goal=None):
    x = wordlist()
    word = None
    round = 1
    while len(x.words) > 1:

        if round > 7:
            if goal:
                pass
                print(f'Failed match {goal}')
            else:
                print('Sorry, we failed :(')
            return 7

        if not word:
            word = "stoae"
        else:
            word=x.choose()
        if goal:
            resp = check_result(word, goal)
        else:
            print(word)
            resp = input()
        for pos in range(len(word)):
            if resp[pos] == "0":
                x.remove(word[pos])
            elif resp[pos] == "1":
                x.sweep(word[pos], pos)
            elif resp[pos] == "2":
                x.fix(word[pos], pos)
        round +=1

    if resp == '22222':
        round -= 1
    if not goal:
        print(f'{x.words[0]} is the correct answer!\nIt took {round} guesses.')
    return round

def test():
    from collections import Counter
    scores = []
    for word in La[:1000]:
        scores.append(play(word))
    print()
    results = Counter(scores)

    for i in range(7):
        i += 1
        try:
            print(f'{i}: {results[i]}')
        except KeyError:
            print(f'{i}: {0}')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '-t':
            test()
    else:
        play()
