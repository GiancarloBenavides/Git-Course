
# 3 bits
'''echo -e "\e[41m color \e[0m"'''
# 4 bits
'''echo -e "\e[101m color \e[0m"'''
# 8 bits
'''echo -e "\e[48;5;196m color \e[0m"'''
# 24 bits
'''echo -e "\e[48;2;255;0;0m color \e[0m"'''


prefix = r"\[\e["
sufix = r"m\]"

colors = {
    "Black": "0",
    "Red": "1",
    "Green": "2",
    "Yellow": "3",
    "Blue": "4",
    "Purple": "5",
    "Cyan": "6",
    "White": "7",
}

expand = {
    # basic
    "username": r"\u",
    "hostname": r"\H",
    "term_num": r"\l",
    "command": r"\#",
    "pwd": r"\W",
    "path": r"\w",
    "shell": r"\s",
    "shell_version": r"\v",
    # other
    "bell": r"\a",
    "newline": r"\n",
    "return": r"\r",
}


def get_colors(bits: int) -> tuple:
    ''' Obtener secuencias de escape para colores. '''
    light = r"1;"
    prefix_foreground = "3"
    prefix_background = "4"
    foreground, background = {}, {}
    for color in colors:
        end = colors[color]+sufix
        foreground_value = prefix+prefix_foreground+end
        foreground_light_value = prefix+light+prefix_foreground+end
        background_value = prefix+prefix_background+end
        background_light_value = prefix+light+prefix_background+end
        foreground.update([[color, foreground_value]])
        foreground.update([["Light " + color, foreground_light_value]])
        background.update([[color, background_value]])
        background.update([["Light " + color, background_light_value]])

    return foreground, background


foreground, background = get_colors(bits=3)

depth = r"$(expr length ${PWD//[!\/]})"
branch = r"$(__git_ps1)"

user_host = foreground["Purple"]+expand["username"]+"@"+expand["hostname"]
directory = foreground["White"]+":"+foreground["Light Blue"] + \
    depth+"/"+expand["pwd"]+foreground["White"]+":"
git = foreground["Yellow"]+branch
prompt = foreground["White"]+"\$>"

ps1 = "PS1='"+user_host+directory+git+prompt+"'"

print(foreground)
print(ps1)
