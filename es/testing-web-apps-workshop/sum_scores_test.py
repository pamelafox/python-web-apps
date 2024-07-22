from summer import sum_scores

def test_sum_empty():
    assert sum_scores([]) == 0

def test_sum_numbers():
    assert sum_scores([8, 9, 7]) == 24