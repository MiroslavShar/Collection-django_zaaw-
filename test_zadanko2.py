import pytest

def prime(n):
    lst = []
    devider = 2
    while n > 1:
        while n % devider == 0:
            lst.append(devider)
            n //= devider
        devider += 1
    # if n % 2 == 0:
    #     lst.append(2)
    #     n //= 2
    # if n > 1:
    #     lst.append(n)
    return lst

    # if n == 3:
    #     return [3]
    # if n == 2:
    #     return [2]
    # return []

@pytest.mark.parametrize('n,result',[
    (1, []),
    (2, [2]),
    (3, [3]),
    (4, [2, 2]),
    (5, [5]),
    (6, [2, 3]),
    (7, [7]),
    (8, [2, 2, 2]),

])

def test_bel(n, result):
    assert prime(n) == result