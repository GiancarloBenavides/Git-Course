prefix=r"\[\033[0"
sufix=r"m\]"

foreground = {
    "Black":"0;30",
    "Dark Gray":"1;30",
    "Light Gray":"0;37",
    "White":"1;37",
    "Blue":"0;34",
    "Light Blue":"1;34",
    "Green":"0;32",
    "Light Green":"1;32",
    "Cyan":"0;36",
    "Light Cyan":"1;36",
    "Red":"0;31",
    "Light Red":"1;31",
    "Purple":"0;35",
    "Light Purple":"1;35",
    "Brown":"0;33",
    "Yellow":"1;33"
}

background = {
    "Black":"0;40",
    "Dark Gray":"1;40",
    "Light Gray":"0;47",
    "White":"1;47",
    "Blue":"0;44",
    "Light Blue":"1;44",
    "Green":"0;42",
    "Light Green":"1;42",
    "Cyan":"0;46",
    "Light Cyan":"1;46",
    "red":"0;41",
    "Light Red":"1;41",
    "Purple":"0;45",
    "Light Purple":"1;45",
    "Brown":"0;43",
    "Yellow":"1;43"
}

for item in foreground:
    foreground[item] = prefix+foreground[item]+sufix

for item in background:
    background[item] = prefix+background[item]+sufix

username=r"\u"
hostname=r"\H"
pwd=r"\W"
path=r"\w"
shell=r"\s"
shell_version=r"\v"
separator=r":"
prompt=r"$ "
branch=r"$(__git_ps1)"
profundidad1=r"$(expr length ${PWD//[!\/]})"
profundidad2=r"$(expr ${PWD//[!\/]} :'.*')"
profundidad3=r"$(echo $str | wc -c)"
profundidad4=r"$(pwd | grep -o '/' - | wc -l)/"
ps1=foreground["Yellow"]+username+foreground["Light Gray"]+separator+foreground["Light Blue"]+profundidad1+"/"+pwd+foreground["Light Gray"]+separator+foreground["Light Red"]+branch+foreground["Light Gray"]
command=f"PS1='{ps1}{prompt}'"

ps1=profundidad2

print(f"Comando prompt:  {command}")