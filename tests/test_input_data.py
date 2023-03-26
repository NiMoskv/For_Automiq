import pytest
from sortirovka.sort_sequency import check_input

case = [
    (['RGB', 'R<G<B'], False),
    (['R G Bm', 'R<G<B'], False),
    (['R', 'R<G<B'], False),
    ([' R', 'R<G<B'], False),
    ([' ', 'R<G<B'], False),

    (['  R  B G   ', 'R<G<B'],
     [['R', 'B', 'G'], {'R': 0, 'G': 1, 'B': 2}]),
    (['R*a B^2 G!', 'R*a<G!<B^2'],
     [['R*a', 'B^2', 'G!'], {'R*a': 0, 'G!': 1, 'B^2': 2}]),
    (['R G', 'R<G<B'], [['R', 'G'], {'R': 0, 'G': 1, 'B': 2}]),
    (['R B', 'R<G<B'], [['R', 'B'], {'R': 0, 'G': 1, 'B': 2}])
]


@ pytest.mark.parametrize("cond, result", case)
def test_answer(cond, result):
    assert check_input(*cond) == result
