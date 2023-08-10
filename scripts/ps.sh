if [[ "${PWD}" == "${HOME}" ]] ; 
then printf \~; 
else echo -n ${PWD##*/}; 
fi
