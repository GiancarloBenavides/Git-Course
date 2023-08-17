prefix = r"\[\e["
light = r"1;"
sufix = r"m\]"
prefix_foreground = 3
prefix_background = 4
foreground, background = {}, {}

colors = {
    "Black": "0",
    "Red": "1",
    "Green": "2",
    "Brown": "3",
    "Blue": "4",
    "Purple": "5",
    "Cyan": "6",
    "White": "7",
    "Custom": "8",
}

foreground = {
    "Black": "0;30",
    "Red": "0;31",
    "Green": "0;32",
    "Brown": "0;33",
    "Blue": "0;34",
    "Purple": "0;35",
    "Cyan": "0;36",
    "Light Gray": "0;37",
    "Custom": "38",

    "Dark Gray": "1;30",
    "Light Red": "1;31",
    "Light Green": "1;32",
    "Yellow": "1;33",
    "Light Blue": "1;34",
    "Light Purple": "1;35",
    "Light Cyan": "1;36",
    "White": "1;37"
}

background = {
    "Black": "0;40",
    "red": "0;41",
    "Green": "0;42",
    "Brown": "0;43",
    "Blue": "0;44",
    "Purple": "0;45",
    "Cyan": "0;46",
    "Light Gray": "0;47",

    "Dark Gray": "1;40",
    "Light Red": "1;41",
    "Light Green": "1;42",
    "Yellow": "1;43",
    "Light Blue": "1;44",
    "Light Purple": "1;45",
    "Light Cyan": "1;46",
    "White": "1;47"
}

for item in foreground:
    foreground[item] = prefix+foreground[item]+sufix

for item in background:
    background[item] = prefix+background[item]+sufix

username = r"\u"
hostname = r"\H"
pwd = r"\W"
path = r"\w"
shell = r"\s"
shell_version = r"\v"

separator = r":"
prompt = r"$ "
branch = r"$(__git_ps1)"
profundidad1 = r"$(expr length ${PWD//[!\/]})"
profundidad2 = r"$(expr ${PWD//[!\/]} :'.*')"
profundidad3 = r"$(echo $str | wc -c)"
profundidad4 = r"$(pwd | grep -o '/' - | wc -l)/"


ps1 = foreground["Yellow"]+username+foreground["Light Gray"]+separator+foreground["Light Blue"]+profundidad1 + \
    "/"+pwd+foreground["Light Gray"]+separator + \
    foreground["Light Red"]+branch+foreground["Light Gray"]
command = f"PS1='{ps1}{prompt}'"

ps1 = profundidad2

print(f"Comando prompt:  {command}")
