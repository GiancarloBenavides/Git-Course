import os
import tomli
import emoji as em

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


def clean_start(message: str) -> str:
    if message[0] == " ":
        message = message[1:]
        clean_start(message)
    return message


def clean_end(message: str) -> str:
    if message[-1] == " " or message[-1] == ".":
        message = message[:-1]
        clean_end(message)
    return message


def clean_commit(commit: str, warn: list):
    len_min = conf["commit"]["minimum_length"]
    len_max = conf["commit"]["maximum_length"]
    r_space = conf["commit"]["required_spaces"]

    position_ds = commit.find("  ")
    if position_ds > 0:
        commit = commit.replace("  ", " ")
        warn.append(MSG["FOR_BODY"])

    if commit[0] == " ":
        warn.append(MSG["FOR_START"])
        commit = clean_start(commit)

    if commit[-1] == " " or commit[-1] == ".":
        warn.append(MSG["FOR_END"])
        commit = clean_end(commit)

    if len(commit) < len_min:
        warn.append(MSG["FOR_MIN"])

    if len(commit) > len_max:
        warn.append(MSG["FOR_MAX"])

    if r_space:
        if commit.find(":") != 0:
            delimiter = commit.find(":")
        else:
            delimiter = commit.find(":", 1)
            if delimiter != -1:
                delimiter = commit.find(":", delimiter+1)

        if delimiter != -1 and not (commit[delimiter+1] == " "):
            warn.append(MSG["FOR_NO_SPACE"])
            commit.replace(":", ": ")

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
    # si no lo encontró y era requerido
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
    response["warnings"] = []
    # os.system('clear').
    conf = load_config()
    commit = load_commit()
    commit = clean_commit(commit, response["warnings"])
    structure, has = get_structure(commit)
    allowed = check_validity(structure, conf)
    response["has"] = has
    response["allowed"] = allowed
    report(debug=True)


if __name__ == "__main__":
    main()
