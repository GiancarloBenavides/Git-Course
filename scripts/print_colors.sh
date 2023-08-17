#!/bin/bash

# 8 standard colors (3 Bits)
function print_color_3_bits() {
    for C in {40..47}; do 
        if [ $C -eq 47 ]; then
            echo -e "\e[30m\e[${C}m $C \e[0m"
        else
            echo -en "\e[37m\e[${C}m $C "
        fi
    done
}

# 16 high intensity colors (4 bits)
function print_color_4_bits() {
    for C in {40..47}; do 
        if [ $C -eq 47 ]; then
            echo -e "\e[30m\e[${C}m 0$C \e[0m"
        else
            echo -en "\e[37m\e[${C}m 0$C "
        fi
    done   
    for C in {100..107}; do 
        if [ $C -eq 107 ]; then
            echo -e "\e[30m\e[${C}m $C \e[0m"
        else
            echo -en "\e[37m\e[${C}m $C "
        fi
    done
}

# 256 colors (8 bits)
function print_color_8_bits() {
    for C in {0..15}; do
        if [ $C -lt 10 ]; then B="0$C"; else B=$C; fi
        if [ $(((C+1)%8)) -eq 0 ]; then
            echo -e "\e[30m\e[48;5;${C}m $B \e[0m"
        else
            echo -en "\e[37m\e[48;5;${C}m $B "
        fi
    done
    for C in {16..255}; do
        if [ $C -lt 100 ]; then B="0$C"; else B=$C; fi
        if [ $(((C+3)%6)) -eq 0 ]; then
            echo -e "\e[30m\e[48;5;${C}m $B \e[0m"
        else
            echo -en "\e[37m\e[48;5;${C}m $B "
        fi
    done
}

# 16_777_216 colors (24 bits)
function print_color_24_bits() {
    for C in {0..255}; do
        if [ $C -le 15 ]; then text=37; else text=30; fi
        if [ $C -lt 10 ]; then 
            B="00$C"
        elif [ $C -lt 100 ]; then
            B="0$C"
        else
            B=$C
        fi
        if [ $(((C+1)%16)) -eq 0 ]; then
            echo -e "\e[${text}m\e[48;2;${C}m $B \e[0m"
        else
            echo -en "\e[${text}m\e[48;2;${C}m $B "
        fi
    done
    for C in {0..255}; do
        if [ $C -le 15 ]; then text=37; else text=30; fi
        if [ $C -lt 10 ]; then 
            B="00$C"
        elif [ $C -lt 100 ]; then
            B="0$C"
        else
            B=$C
        fi
        if [ $(((C+1)%16)) -eq 0 ]; then
            echo -e "\e[${text}m\e[48;2;0;${C}m $B \e[0m"
        else
            echo -en "\e[${text}m\e[48;2;0;${C}m $B "
        fi
    done
    for C in {0..255}; do
        if [ $C -le 15 ]; then text=37; else text=30; fi
        if [ $C -lt 10 ]; then 
            B="00$C"
        elif [ $C -lt 100 ]; then
            B="0$C"
        else
            B=$C
        fi
        if [ $(((C+1)%16)) -eq 0 ]; then
            echo -e "\e[${text}m\e[48;2;0;0;${C}m $B \e[0m"
        else
            echo -en "\e[${text}m\e[48;2;0;0;${C}m $B "
        fi
    done
}

if [ $# -ne 1 ]; then
    print_color_4_bits
else
    if [ $1 -eq 3 ]; then
        print_color_3_bits
    elif [ $1 -eq 8 ]; then
        print_color_8_bits
    elif [ $1 -eq 24 ]; then
        print_color_24_bits
    else
        print_color_4_bits
    fi
fi
