# TDD
# 1. test: Escribir la prueba
# 2. validar: Ejecutar la prueba
# 3. refactoring: Implementar la funcionalidad
from .structure import get_structure


def test_has_emoji_found():
    str, has = get_structure("⚠️")
    assert has["emoji"] == True


def test_has_emoji_no_found():
    str, has = get_structure("only text")
    assert has["emoji"] == False


def test_has_type_delimiter_found():
    str, has = get_structure("type:")
    assert has["type"] == True


def test_has_type_delimiter_no_found():
    str, has = get_structure("feat")
    assert has["type"] == False


def test_has_scope_found():
    str, has = get_structure("(scope)")
    assert has["scope"] == True


def test_has_scope_only_open():
    str, has = get_structure("(api")
    assert has["scope"] == False


def test_has_scope_only_close():
    str, has = get_structure("api)")
    assert has["scope"] == False


def test_has_scope_first_close():
    str, has = get_structure("api)(")
    assert has["scope"] == False


def test_has_message():
    str, has = get_structure("type: new endpoint")
    assert has["message"] == True


def test_has_message_no_found():
    str, has = get_structure("type(scope):")
    assert has["message"] == False


def test_has_message_with_emoji():
    str, has = get_structure("⚠️ new endpoint")
    assert has["message"] == True


def test_has_message_with_emoji_no_found():
    str, has = get_structure("⚠️ (api)")
    assert has["message"] == False


def test_has_message_only_emoji():
    str, has = get_structure("⚠️")
    assert has["message"] == False
