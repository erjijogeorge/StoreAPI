def test_add_two():
    x = 1
    y = 2
    assert x + y == 3


def test_dict_contains():
    dict_xvalues = {"x": 1, "y": 2}
    expected = {"x": 1}

    assert expected.items() <= dict_xvalues.items()
