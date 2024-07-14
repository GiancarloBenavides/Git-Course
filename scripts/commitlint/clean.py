def remove_double_spaces(message: str) -> str:
    if message.count("  "):
        message = remove_double_spaces(message.replace("  ", " "))

    return message


def clean_start(message: str) -> str:
    if message[0] == " ":
        message = clean_start(message[1:])

    return message


def clean_end(message: str) -> str:
    if message[-1] == " " or message[-1] == ".":
        message = clean_end(message[:-1])

    return message


def has_no_required_type_spaces(message: str, delimiter: str = ":") -> bool:
    if len(delimiter) == 1:
        if message.find(delimiter) != 0:
            position = message.find(delimiter)
        else:
            position = message.find(delimiter, 1)
            if position != -1:
                position = message.find(delimiter, position+1)

    return position != -1 and not (message[position+1] == " ")


def has_no_required_scope_spaces(message: str, start: str = "(", end: str = ")") -> tuple[bool, bool]:
    start = message.find(start)
    end = message.find(end)

    if start > 0 and end > 0 and end > start:
        return message[start-1] != " ", message[end+1] != " "

    return False, False


def clean_commit(commit: str, warn: list, conf: dict, locals: dict):
    required_type_spaces = conf["component"]["type"]["required_end_spaces"]
    required_scope_spaces = conf["component"]["scope"]["required_spaces"]

    if commit.find("  ") >= 0:
        warn.append(locals["FOR_BODY"])
        commit = remove_double_spaces(commit)

    if commit[0] == " ":
        warn.append(locals["FOR_START"])
        commit = clean_start(commit)

    if commit[-1] == " " or commit[-1] == ".":
        warn.append(locals["FOR_END"])
        commit = clean_end(commit)

    len_min = conf["commit"]["minimum_length"]
    len_max = conf["commit"]["maximum_length"]
    if len(commit) < len_min:
        warn.append(locals["FOR_MIN"])

    if len(commit) > len_max:
        warn.append(locals["FOR_MAX"])

    delimiter = conf["component"]["type"]["split_delimiter"]
    if required_type_spaces and has_no_required_type_spaces(commit, delimiter):
        warn.append(locals["FOR_NO_SPACE"])
        commit = commit.replace(delimiter, delimiter+" ")

    start = conf["component"]["scope"]["start_delimiter"]
    end = conf["component"]["scope"]["end_delimiter"]
    spaces = has_no_required_scope_spaces(commit, start, end)
    if required_scope_spaces and (spaces[0] or spaces[1]):
        warn.append(locals["FOR_NO_SPACE"])
        if spaces[0]:
            commit = commit.replace(start, " "+start)
        
        if spaces[1]:
            commit = commit.replace(end, end+" ")

    return commit
