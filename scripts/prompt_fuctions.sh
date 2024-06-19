#!/bin/bash

# FUNCIONES PARA IMPLEMENTAR EN EL PROMPT DE LA TERMINAL BASH
# Script de funciones que se pueden implementar en el prompt.
# Incluir en ~/.bashrc 


# Get the exit code of the last command
function nonzero_return() {
    if [[ "${PWD}" == "${HOME}" ]] ; 
    then
        printf \~;
    else
        if [[ ${PWD} == / ]]; 
        then 
            printf /;
        else 
            echo -n ${PWD##*/}; 
        fi 
    fi
}

# Get the exit code of the last command
function __depth() {
    if [[ ${PWD} != / ]] || [[ ${PWD} != ${HOME} ]];
    then echo -n "$(expr length ${PWD//[!\/]})/";
    fi
}



# Get the exit code of the last command (get_last_error)
function nonzero_return() {
    local RETVAL=$?
    if [[ $RETVAL -ne 0 ]]
    then
        echo "❌($RETVAL)"
    else
        echo "✅"
    fi
}





for C in {100..107}; do
    echo -en "\e[${C}m$C "
done

# standard colors (8 Bits)
for C in {0..255}; do
    tput setab $C
    echo -n "$C "
done
tput sgr0
echo


# 256 colors (8 bits)
for C in {16..255}; do
    echo -en "\e[48;5;${C}m$C "
done
echo -e "\e(B\e[m"


# 16_777_216 colors (24 bits)
for C in {0..255}; do
    echo -en "\e[48;2;${C};0;0m C-$C "
done
echo -e "\e(B\e[m"