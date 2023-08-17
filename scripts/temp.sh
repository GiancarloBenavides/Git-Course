#!/bin/bash

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

function __depth() {
    if [[ ${PWD} != / ]] || [[ ${PWD} != ${HOME} ]];
    then echo -n "$(expr length ${PWD//[!\/]})/";
    fi
}

function nonzero_return() {
    local RETVAL=$?
    if [[ $RETVAL -ne 0 ]]
    then
        echo "❌($RETVAL)"
    else
        echo "✅"
    fi
}


# standard colors (3 Bits)
for C in {40..47}; do 
    if [ $C -eq 47 ]; then
        echo -e "\e[30m\e[${C}m 0$C \e[0m"
    else
        echo -en "\e[37m\e[${C}m 0$C "
    fi
done
# high intensity colors (4 bits)
for C in {100..107}; do 
    if [ $C -eq 107 ]; then
        echo -e "\e[30m\e[${C}m $C \e[0m"
    else
        echo -en "\e[37m\e[${C}m $C "
    fi
done


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