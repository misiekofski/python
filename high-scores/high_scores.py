class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        return max(self.scores)

    def personal_top_three(self):
        self.scores.sort(reverse=True)
        return self.scores if (len(self.scores)<4) else (self.scores[:3])