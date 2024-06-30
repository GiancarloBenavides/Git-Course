import os
import tomli
import emoji as em

from messages import es as MSG

conf, structure, response = {}, {}, {}


def load_config(file="config.toml"):
    with open(file, "rb") as f:
        data = tomli.load(f)
        return data.copy()


def load_commit_structure(commit: str):
    structure["emoji"] = None
    structure["type"] = None
    structure["scope"] = None
    structure["message"] = commit


def load_commit():
    commit = input(MSG["MSG_INPUT"] + ' [↓] \n')
    if len(commit) <= 2:
        load_commit()

    return commit


def clean_commit(commit: str):
    if commit[0] == " ":
        commit = commit[1:]
        commit = clean_commit(commit)

    if commit[-1] == " " or commit[-1] == ".":
        commit = commit[:-1]
        commit = clean_commit(commit)

    return commit


def commit_has_emoji() -> bool:
    pattern: str = structure["message"]
    has_emoji = em.is_emoji(pattern[0])
    if has_emoji:
        structure["emoji"] = [pattern[0], em.demojize(pattern[0]), True]
        structure["message"] = pattern[1:]
        return has_emoji

    if pattern[0] == ":" and pattern.count(":") >= 2:
        split_pattern = pattern.split(":")
        emoji_text = f":{split_pattern[1]}:"
        emoji = em.emojize(emoji_text)

        if len(emoji) == 1:
            structure["emoji"] = [emoji, emoji_text, False]
            structure["message"] = split_pattern[2]
            has_emoji = True

    return has_emoji


def commit_has_type(delimiter: str = ":") -> bool:
    msg: str = structure["message"]
    has_type = msg.count(delimiter) >= 1
    if has_type:
        split_msg = msg.split(delimiter)
        structure["type"] = split_msg[0]
        structure["message"] = split_msg[1]
    return has_type


def commit_has_scope() -> bool:
    msg: str = structure["type"] if structure["type"] != None else structure["message"]
    pattern = msg.split(":")[0] if msg.count(":") >= 1 else msg
    has_scope = bool(pattern.count("(") and pattern.count(")"))
    if has_scope:
        start_scope = pattern.index("(")
        end_scope = pattern.index(")")
        structure["scope"] = pattern[start_scope+1:end_scope]
        if structure["type"] == None:
            structure["message"] = pattern[end_scope + 1:]
            return True

        structure["type"] = pattern[:start_scope]
    return has_scope


def commit_has_message() -> bool:
    msg: str = structure["message"]
    has_message = len(msg) >= 2
    if not has_message:
        structure["message"] = None

    return has_message


def check_emoji() -> bool:
    check = False
    emj: str = structure["emoji"][0]
    for key in conf['types']:
        for index, emoji in enumerate(conf['types'][key]):
            if emj == emoji:
                return True
    return check


def check_type() -> bool:
    tpy: str = structure["type"]
    check = tpy in conf['types']
    return check


def check_scope() -> bool:
    scp: str = structure["scope"]
    check = scp in conf['scopes']['values']
    return check


def check_message() -> bool:
    check = False
    msg: str = structure["message"]
    if len(msg) > 0 and msg[0] == " ":
        structure["message"] = structure["message"][1:]
        if len(msg) > 1 and msg[1].islower():
            return True

    return check


def report():
    pass


def main():
    global conf
    has, allowed = {}, {}
    os.system('clear')
    conf = load_config()
    commit = load_commit()
    commit = clean_commit(commit)
    load_commit_structure(commit)
    has["emoji"] = commit_has_emoji()
    has["type"] = commit_has_type()
    has["scope"] = commit_has_scope()
    has["message"] = commit_has_message()
    allowed["emoji"] = check_emoji() if has["emoji"] else False
    allowed["type"] = check_type()
    allowed["scope"] = check_scope()
    allowed["message"] = check_message() if has["message"] else False
    response["has"] = has
    response["allowed"] = allowed
    report()


if __name__ == "__main__":
    main()
    print("Estructura  : ", structure)
    print("has         : ", response["has"])
    print("allowed     : ", response["allowed"])
