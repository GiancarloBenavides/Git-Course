# TDD
# 1. test: Escribir la prueba
# 2. validar: Ejecutar la prueba
# 3. refactoring: Implementar la funcionalidad
from .check import check_emoji, check_type, check_scope, check_message, check_validity

conf = {'title': 'TOML config',
        'commit': {
            'minimum_length': 7,
            'maximum_length': 50,
            'allowed_capitalize': False,
            'required_spaces': True,
            'show_clean': True,
            'show_warning': True},
        'component': {
            'emoji': {'allowed': True, 'required': True, 'any_values': False},
            'type': {'allowed': False, 'required': False, 'any_values': False},
            'scope': {'allowed': True, 'required': True, 'any_values': False}},
        'types': {
            'BREAKING': [':boom:', '💥'],
            'feat': [':sparkles:', '✨'],
            'fix': [':ladybird:', '🐞'],
            'refactor': [':recycle:', '♻️'],
            'chore': [':gear:', '⚙️']},
        'scopes': {'values': ['api', 'web', 'app']}}


def test_check_emoji_found():
    assert check_emoji("✨", conf['types']) == True


def test_check_emoji_no_found():
    assert check_emoji("💫", conf['types']) == False


def test_check_type_found():
    assert check_type("feat", conf['types']) == True


def test_check_type_no_found():
    assert check_type("test", conf['types']) == False


def test_check_scope_found():
    assert check_scope("api", conf['scopes']['values']) == True


def test_check_scope_no_found():
    assert check_scope("frontend", conf['scopes']['values']) == False


def test_check_message_found():
    assert check_message("new endpoint") == True


def test_check_message_no_found():
    assert check_message("") == False
