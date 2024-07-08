import emoji as em


def load_commit_structure(commit: str) -> dict:
    structure = {}
    structure["emoji"] = ""
    structure["type"] = ""
    structure["scope"] = ""
    structure["message"] = commit
    return structure


def commit_has_emoji(structure: dict) -> bool:
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


def commit_has_type(structure: dict, delimiter: str = ":") -> bool:
    msg: str = structure["message"]
    has_type = msg.count(delimiter) >= 1
    if has_type:
        split_msg = msg.split(delimiter)
        structure["type"] = split_msg[0]
        structure["message"] = split_msg[1]
    return has_type


def commit_has_scope(structure: dict) -> bool:
    msg: str = structure["type"] if structure["type"] != "" else structure["message"]
    pattern = msg.split(":")[0] if msg.count(":") >= 1 else msg
    has_scope = bool(pattern.count("(") and pattern.count(")"))
    if has_scope:
        start_scope = pattern.index("(")
        end_scope = pattern.index(")")
        if end_scope < start_scope:
            return False

        structure["scope"] = pattern[start_scope+1:end_scope]
        if structure["type"] == "":
            structure["message"] = pattern[end_scope + 1:]
            return True

        structure["type"] = pattern[:start_scope]
    return has_scope


def commit_has_message(structure: dict) -> bool:
    msg: str = structure["message"]
    has_message = len(msg) >= 2
    if has_message:
        structure["message"] = msg[1:]

    return has_message


def get_structure(commit: str):
    has = {}
    structure = load_commit_structure(commit)
    has["emoji"] = commit_has_emoji(structure)
    has["type"] = commit_has_type(structure)
    has["scope"] = commit_has_scope(structure)
    has["message"] = commit_has_message(structure)
    return structure, has
