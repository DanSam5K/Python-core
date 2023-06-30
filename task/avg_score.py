from typing import List
from dataclasses import dataclass

@dataclass
class Score:
    name: str
    number: int

    def __repr__(self) -> str:
        return f"{type(self).__name__}{self.name, self.number}"
       


def get_best_avg_score(scores: List[Score]) -> Score:
    # calculate sum and count for each name
    score_dict = sum_and_count(scores)
    # calculate average score
    a_scores = average_score(score_dict)
    # Find the score with the highest average
    best_avg_name = max(a_scores, key=a_scores.get)
    best_avg_score = a_scores[best_avg_name]
    return Score(best_avg_name, best_avg_score)



def sum_and_count(arg):
    score_dict = {}
    for score in arg:
        if score.name not in score_dict:
            score_dict[score.name] = {'sum': score.number, 'count': 1}
        else:
            score_dict[score.name]['sum'] += score.number
            score_dict[score.name]['count'] += 1
    return score_dict

def average_score(arg):
    avg_score = {
        name: arg[name]['sum']/arg[name]['count']
        for name in arg
    }
    return avg_score

def main():
    scores = [
        Score("Name1", 80),
        Score("Name2", 67),
        Score("Name1", 60)
    ]

    best_avg_score = get_best_avg_score(scores)
    print(best_avg_score)


if __name__ == '__main__':
    main()
