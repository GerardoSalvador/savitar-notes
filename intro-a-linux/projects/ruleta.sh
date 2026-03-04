#!/bin/bash

greenColour="\e[0;32m\033[1m"
redColour="\e[0;31m\033[1m"
blueColour="\e[0;34m\033[1m"
yellowColour="\e[0;33m\033[1m"
purpleColour="\e[0;35m\033[1m"
turquoiseColour="\e[0;36m\033[1m"
grayColour="\e[0;37m\033[1m"
endColour="\033[0m\e[0m"

function ctrl_c(){
  echo -e "\n${redColour}[!] Saliendo...${endColour}"
  tput cnorm
  exit 1
}

# Ctrl+C
trap ctrl_c INT

function helpPanel(){
  echo -e "\n${yellowColour}[+]${endColour}${grayColour} Panel de ayuda:${endColour}"
  echo -e "\t${turquoiseColour}m)${endColour}${grayColour} Dinero con el que se desea iniciar a jugar${endColour}"
  echo -e "\t${turquoiseColour}t)${endColour}${grayColour} Técnica con la que se desea jugar${endColour}${greenColour} (martingala/inverseLabrouchere)${endColour}"
  echo -e "\t${turquoiseColour}h)${endColour}${grayColour} Muestra el panel de ayuda${endColour}"
  exit 1
}

function martingala(){
  echo -e "\n[+] Dinero actual: $money"
  echo -ne "\n[+] ¿Cuánto dinero tienes pensado apostar? -> " && read initial_bed
  echo -ne "\n[+] ¿A que deseas apostar continuamente (par/impar)? -> " && read par_impar

 # echo -e "\n${yellowColour}[+]${endColour}${grayColour} Vamos a jugar con la cantidad inicial de${endColour}${yellowColour} $initial_bed${endColour}${grayColour} a${endColour}${yellowColour} $par_impar${endColour}"

  backup_bet=$initial_bet
  play_counter=1
  jugadas_malas=""

  tput civis # Ocultar el cursor
  while true; do
    money=$(($money-$initial_bet))
    random_number="$(($RANDOM % 37))"

    if [ ! "$money" -lt 0 ]; then
      if [ "$par_impar" == "par" ]; then
        # Toda está definición es para cuando apostamos a números pares
        echo $random_number
        if [ "$(($random_number % 2))" -eq 0 ]; then
          if [ "$random_number" -eq 0 ]; then
            initial_bet=$(($initial_bet*2))
            jugadas_malas+="$random_number "
          else
            reward=$(($initial_bet*2))
            money=$(($money+$reward))
            initial_bet=$backup_bet
            jugadas_malas=""
          fi
        else
          initial_bet=$(($initial_bet*2))
          jugadas_malas+="$random_number "
        fi
      else
        if [ "$(($random_number % 2))" -eq 1 ]; then
          reward=$(($initial_bet*2))
          money=$(($money+$reward))
          initial_bet=$backup_bet
          jugadas_malas=""
        else
          initial_bet=$(($initial_bet*2))
          jugadas_malas+="$random_number"
        fi
      fi
    else
      echo -e "[!] Te has quedado sin pasta cabrón"
      echo -e "[+] Han habido un total de (($play_counter-1)) jugadas consecutivas que han salido:"
      echo -e "[+] A continuación se van a representar las"
      echo -e "[ $jugadas_malas ]"
      tput cnorm; exit 0
    fi
    
    let play_counter+=1
  done
  tput cnorm # Recuperamos el cursor
}

while getopts "m:t:h" arg; do
  case $arg in
    m) money=$OPTARG;;
    t) technique=$OPTARG;;
    h) helpPanel;;
  esac
done

if [ "$money" ] && [ $technique ]; then
  if [ "$technique" == "martingala" ]; then
    martingala
  else
    echo -e "\n${redColour}[!] La técnica introducida no existe!!!${endColour}"
    helpPanel
  fi
else
  helpPanel
fi

