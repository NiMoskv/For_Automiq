import pytest
from sortirovka.sort_sequency import sort_input

case = [
    ([' R G B B G R ', 'R<G<B'], 'R R G G B B'),
    (['Red G B B G Red', 'Red<G<B'], 'Red Red G G B B'),
    (['Red G B B G Red', 'Red<G<B'], 'Red Red G G B B'),
    (['R G B B G R Z D D', 'R>G>B>D>Z'], 'Z D D B B G G R R'),
    (['R G B B G R D D', 'R>G>B>D>Z'], 'D D B B G G R R'),
    (['R G B B G R Z D D', 'R>G>B>D'], False),
    (['R G B B G R Z D D', 'R>G>B>D<Z'], False),
    (['R G B B G R Z D D', '>G>B>D>Z'], False),
    (['R G B B G R Z D D', 'R>G>B>D>'], False),
    (['R G B B G R Z D D', 'R>G>B=D>Z'], False),



]


@pytest.mark.parametrize("data, result", case)
def test_app(data, result):
    assert sort_input(*data) == result
