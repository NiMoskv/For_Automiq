import pytest
from sortirovka.sort_sequency import parcer_condition

case = [
    ('<<<G<B', False),
    ('<G<B', False),
    ('R<G<B<<<<', False),
    ('R<G,B<', False),
    ('R<G>B', False),
    ('R<<<<<<<G<B', False),
    ('R<G<<<<B', False),
    ('R<g<R<B', False),
    ('G>B>R>G', False),
    ('R<=G<B', False),
    ('r<G<=B', False),
    ('R=G<B', False),
    ('R<R<G< ', False),
    (' <B<G', False),
    ('RG', False),
    ('RED<GREEN<BLUE', {'RED': 0, 'GREEN': 1, 'BLUE': 2}),
    ('red<green<blue', {'red': 0, 'green': 1, 'blue': 2}),
    ('reD<grEEn<bLuE', {'reD': 0, 'grEEn': 1, 'bLuE': 2}),
    ('r<R<G<g<B<b', {'r': 0, 'R': 1, 'G': 2, 'g': 3, 'B': 4, 'b': 5}),
    ('1<B<G', {'1': 0, 'B': 1, 'G': 2}),
    ('R<B <G', {'R': 0, 'B': 1, 'G': 2}),
    ('R  < B<   G', {'R': 0, 'B': 1, 'G': 2}),
    ('   R<B<G   ', {'R': 0, 'B': 1, 'G': 2}),
    ('R*<B^2<G#', {'R*': 0, 'B^2': 1, 'G#': 2}),


]


@pytest.mark.parametrize("cond, result", case)
def test_answer(cond, result):
    assert parcer_condition(cond) == result
