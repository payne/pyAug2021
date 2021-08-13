def test_least_number_of_votes():
    votes = {'java': 10_000, 'python': 100_000, 'c': 1000}
    least = least_number_of_votes(votes)
    assert 1000 == least


def least_number_of_votes(votes_dictionary):
    return min(votes_dictionary.values())
