import csv
from io import StringIO
from typing import List, Any


class Ballot:
    def __init__(self, choices):
        self.choices = choices
        self.current_choice = 0

    def choice(self):
        return self.choices[self.current_choice]

    def next_choice(self):
        # TODO: Error checking
        self.current_choice += 1

    def __repr__(self):
        return ",".join(self.choices)


def read_ballots(multiline_csv_string):
    ballots = []
    print(multiline_csv_string)
    input_file = StringIO(multiline_csv_string)
    csv_reader = csv.reader(input_file, delimiter=",")
    for row in csv_reader:
        ballots.append(Ballot(row))
    return ballots


def count_votes_old(ballots):
    v = {}
    for b in ballots:
        if b.choice() not in v:
            v[b.choice()] = 0
        v[b.choice()] += 1
    return v


def count_votes(ballots):
    return {
        b.choice(): [bc.choice() for bc in ballots].count(b.choice()) for b in ballots
    }


def adjust_ballots(ballots):
    votes = count_votes(ballots)
    print(f"In adjust_ballots: votes={votes}")
    counts = list(votes.values())
    counts.sort()
    lowest = counts[0]
    for b in ballots:
        old_choice = b.choice()
        choice_count = votes[old_choice]
        if choice_count == lowest:
            b.next_choice()
            print(f"{old_choice} only got {choice_count} votes, so ", end="")
            print(f"adjusted ballot: {b} choice is now {b.choice()}")


def main():
    ballots_string = """red,green,blue,yellow
blue,green,yellow,red
yellow,green,blue,red
purple,green,red,yellow
"""
    global ballots
    ballots = read_ballots(ballots_string)
    print(f"There are {len(ballots)} ballots.")
    assert 4 == len(ballots)
    print("Ballots are:")
    for b in ballots:
        print(f"\t{b}")
    to_win = len(ballots) / 2.0
    votes = {}
    winner = []
    round_number = 1
    while len(winner) == 0:
        if len(votes) > 0:
            adjust_ballots(ballots)
        votes = count_votes(ballots)
        print(f"In round {round_number} votes={votes}")
        # https://www.freecodecamp.org/news/list-comprehension-in-python/
        winner = [canidate for canidate in votes.keys() if votes[canidate] >= to_win]
        round_number += 1

    print(f"winner={winner[0]}")


if __name__ == "__main__":
    # execute only if run as a script
    main()
