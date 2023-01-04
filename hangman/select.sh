#!/bin/bash

PS3='Please enter your choice: '
options=("CLI" "GUI" "QUIT")
select opt in "${options[@]}"; do
    case $opt in
        "CLI")
            bash cli/run.sh
            ;;
        "GUI")
            bash gui/run.sh
            ;;
        "QUIT")
            break
            ;;
        *) echo "invalid option $REPLY";;
    esac
    REPLY=
done
