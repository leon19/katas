from app.reverser import reverse


def test_correctly_reverse_string():
    assert reverse('hola') == 'aloh'
    assert reverse('echo') == 'ohce'
