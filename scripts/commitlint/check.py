def check_emoji(emoji: str, allowed: list) -> bool:
    check = False
    if not emoji:
        return False
    
    for key in allowed:
        for index, item in enumerate(allowed[key]):
            if emoji == item:
                return True
    return check


def check_type(type: str, allowed: list) -> bool:
    check = type in allowed
    return check


def check_scope(scope: str, allowed: list) -> bool:
    check = scope in allowed
    return check


def check_message(message: str) -> bool:
    return len(message) >= 1


def check_validity(structure: dict, conf: dict):
    allowed = {}
    allowed["emoji"] = check_emoji(structure["emoji"][0], conf['types'])
    allowed["type"] = check_type(structure["type"], conf['types'])
    allowed["scope"] = check_scope(
        structure["scope"], conf['scopes']['values'])
    allowed["message"] = check_message(structure["message"])
    return allowed
