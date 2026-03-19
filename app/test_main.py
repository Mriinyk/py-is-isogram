from app.main import is_isogram


def test_is_isogram() -> None:
    assert is_isogram("hell")
    assert is_isogram("Hello")
    assert is_isogram("hi")
    assert is_isogram("word")
    assert is_isogram("play")
    assert is_isogram("run")
    assert is_isogram("test")
    assert is_isogram("Heroes")
    assert is_isogram("darkness")
    assert is_isogram("man")
    assert is_isogram("woman")
    assert is_isogram("papa")
    assert is_isogram("mama")
    assert is_isogram("pip")
    assert is_isogram("python")
    assert is_isogram("digital")
    assert is_isogram("ark")
    assert is_isogram("night")
