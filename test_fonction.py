from main import main1, main2
from fonction import intervale, fake_id1, fake_id2

L = [
    11,
    22,
    95,
    115,
    998,
    1012,
    1188511880,
    1188511890,
    222220,
    222224,
    1698522,
    1698528,
    446443,
    446449,
    38593856,
    38593862,
    565653,
    565659,
    824824821,
    824824827,
    2121212118,
    2121212124,
]


def test_main1():
    assert main1(L) == 1227775554


def test_main2():
    assert main2(L) == 4174379265


test_main1()
test_main2()
