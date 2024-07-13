import os
import tomli
import emoji as em

from clean import clean_commit
from structure import get_structure
from validate import check_validity
from messages import es as MSG

conf, structure, response = {}, {}, {}


def load_config(file="config.toml"):
    with open(file, "rb") as f:
        data = tomli.load(f)
        return data.copy()


def load_commit():
    commit = input(MSG["FOR_INPUT"] + ' [↓] \n')
    if len(commit) <= 2:
        load_commit()

    return commit


def show_warnings(warnings: list):
    count = len(warnings)
    for warn in warnings:
        print("⚠️  ", warn)
    return count


def report(debug: bool = False):
    errors = 0
    print("--"*25)

    if not response["has"]["message"]:
        errors += 1
        print("❌  ", MSG["FOR_EMPTY"])

    # ---------------------
    # si encontró un emoji
    if response["has"]["emoji"]:
        # si no era permitido
        if not conf["component"]["emoji"]["allowed"]:
            errors += 1
            print("❌  ", MSG["EMJ_NOT_EMPTY"])
        # si los permitidos no eran todos y el tipo encontrado no estaba entre los permitidos
        if not conf["component"]["emoji"]["any_values"] and not response["allowed"]["emoji"]:
            errors += 1
            print("❌  ", MSG["EMJ_NOT_ALLOWED"])
    # sfix i no lo encontró y era requerido
    elif conf["component"]["emoji"]["required"]:
        errors += 1
        print("❌  ", MSG["EMJ_EMPTY"])

    # --------------------
    # si encontró un tipo
    if response["has"]["type"]:
        if not conf["component"]["type"]["allowed"]:
            errors += 1
            print("❌  ", MSG["TYP_NOT_EMPTY"])
        if not conf["component"]["type"]["any_values"] and not response["allowed"]["type"]:
            errors += 1
            print("❌  ", MSG["TYP_NOT_ALLOWED"])
    elif conf["component"]["type"]["required"]:
        errors += 1
        print("❌  ", MSG["TYP_EMPTY"])

    # ---------------------
    # si encontró un scope
    if response["has"]["scope"]:
        if not conf["component"]["scope"]["allowed"]:
            errors += 1
            print("❌  ", MSG["SCP_NOT_EMPTY"])
        if not conf["component"]["scope"]["any_values"] and not response["allowed"]["scope"]:
            errors += 1
            print("❌  ", MSG["SCP_NOT_ALLOWED"])
    elif conf["component"]["scope"]["required"]:
        errors += 1
        print("❌  ", MSG["SCP_EMPTY"])

    warnings = show_warnings(response["warnings"])
    if errors+warnings > 0:
        print("--"*25)
        print("❌", MSG["FOR_ERROR"], "->", errors, "     ",
              "⚠️", MSG["FOR_WARN"], "->", warnings)
    else:
        print(MSG["FOR_OK"])

    print("--"*25)

    if debug:
        print("Estructura  : ", structure)
        print("has         : ", response["has"])
        print("allowed     : ", response["allowed"])
        print("warnings    : ", response["warnings"])


def main():
    global conf, structure
    has, allowed = {}, {}
    warn = []
    # os.system('clear').
    conf = load_config()
    commit = load_commit()
    commit = clean_commit(commit, warn, conf)
    structure, has = get_structure(commit)
    allowed = check_validity(structure, conf)
    response["warnings"] = warn
    response["has"] = has
    response["allowed"] = allowed
    report(debug=True)


if __name__ == "__main__":
    main()
