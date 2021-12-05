class LSystem:

    def __init__(self, axiom, rules, alphabet, iteration):
        self.axiom = axiom
        self.rules = rules
        self.alphabet = alphabet
        self.iteration = iteration
        pass

    def process(self):
        inp = self.axiom
        for n in range(self.iteration):
            out = ""
            pos = 0
            while pos < len(inp):
                old_pos = pos
                for (fr, to) in self.rules:
                    if pos + len(fr) <= len(inp):
                        c = inp[pos:pos + len(fr)]
                        if c == fr:
                            out = out + to
                            pos = pos + len(fr)
                            break
                if pos == old_pos:
                    out = out + inp[pos:pos + 1]
                    pos = pos + 1
            inp = out

        return out

    def add_alphabet(self, a, func):
        self.alphabet[a] = func

    def draw(self):
        generated = self.process()
        for a in generated:
            self.alphabet[a]()
