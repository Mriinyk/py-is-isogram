from app.main import is_isogram


def test_is_isogram() -> None:
    assert is_isogram("playgrounds")
    assert is_isogram("")
    assert is_isogram("hi")
    assert is_isogram("word")
    assert is_isogram("play")
    assert is_isogram("run")
    assert is_isogram("man")
    assert is_isogram("woman")
    assert is_isogram("python")
    assert is_isogram("ark")
    assert is_isogram("night")
