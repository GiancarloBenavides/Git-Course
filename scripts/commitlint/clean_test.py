# TDD
# 1. test: Escribir la prueba
# 2. validar: Ejecutar la prueba
# 3. refactoring: Implementar la funcionalidad
from .clean import *


def test_remove_double_spaces():
    message = "   message  width  errors..."
    new_message = remove_double_spaces(message)
    assert new_message == " message width errors..."


def test_clean_start():
    message = "   message  width  errors..."
    new_message = clean_start(message)
    assert new_message == "message  width  errors..."


def test_clean_end():
    message = "   message  width  errors..."
    new_message = clean_end(message)
    assert new_message == "   message  width  errors"


def test_remove_point_and_spaces():
    message = "   message   width  error.. ."
    new_message = remove_double_spaces(clean_end(clean_start(message)))
    assert new_message == "message width error"


def test_has_no_required_type_spaces_true():
    assert has_no_required_type_spaces("message:without space") == True


def test_has_no_required_type_spaces_false():
    assert has_no_required_type_spaces("message: without space") == False


def test_has_no_required_scope_spaces_true():
    assert has_no_required_scope_spaces(
        "message(without)space") == (True, True)


def test_has_no_required_scope_spaces_true_false():
    assert has_no_required_scope_spaces(
        "message(without) space") == (True, False)


def test_has_no_required_scope_spaces_false():
    assert has_no_required_scope_spaces(
        "message (without) space") == (False, False)
