#export R_LIBS=$HOME/R
#alias R='R --no-save --no-restore-data --quiet'

#export INPUTRC=~/.inputrc 
#export EDITOR="gedit" 

# Save lots of history 
export HISTFILESIZE=10000 
export HISTSIZE=10000 
export HISTCONTROL=erasedups 
#shopt -s histappend 

# Show which directory you're working in 
#export PS1="\W: "


#Work
export PATH=$PATH:~/Dropbox/work/scripts
export PATH=$PATH:/Users/kevinlin/Dropbox/code/lib/custom/libPython


#Custom Code:
alias ll='ls -l'
alias home="~"
alias ssh_aws="ssh -i ~/.ec2/pk-test.pem ubuntu@ec2-50-19-126-151.compute-1.amazonaws.com"

function today {
    echo "Today's date is:"
    date +"%A, %B %-d, %Y"
}

_autojump() 
{
        local cur
        cur=${COMP_WORDS[*]:1}
	echo date >> autojump.log
	echo $cur >> autojump.log
        while read i
        do
            COMPREPLY=("${COMPREPLY[@]}" "${i}")
	    echo $COMPREPLY >>autojump.log
	    echo "===" >> autojump.log
        done  < <(autojump --bash --completion $cur)
}
complete -F _autojump j
data_dir=$([ -e ~/.local/share ] && echo ~/.local/share || echo ~)
export AUTOJUMP_HOME=${HOME}
if [[ "$data_dir" = "${HOME}" ]]
then
    export AUTOJUMP_DATA_DIR=${data_dir}
else
    export AUTOJUMP_DATA_DIR=${data_dir}/autojump
fi
if [ ! -e "${AUTOJUMP_DATA_DIR}" ]
then
    mkdir "${AUTOJUMP_DATA_DIR}"
    mv ~/.autojump_py "${AUTOJUMP_DATA_DIR}/autojump_py" 2>>/dev/null #migration
    mv ~/.autojump_py.bak "${AUTOJUMP_DATA_DIR}/autojump_py.bak" 2>>/dev/null
    mv ~/.autojump_errors "${AUTOJUMP_DATA_DIR}/autojump_errors" 2>>/dev/null
fi

AUTOJUMP='{ [[ "$AUTOJUMP_HOME" == "$HOME" ]] && (autojump -a "$(pwd -P)"&)>/dev/null 2>>${AUTOJUMP_DATA_DIR}/autojump_errors;} 2>/dev/null'
if [[ ! $PROMPT_COMMAND =~ autojump ]]; then
  export PROMPT_COMMAND="${PROMPT_COMMAND:-:} ; $AUTOJUMP"
fi 
alias jumpstat="autojump --stat"
function j { new_path="$(autojump $@)";if [ -n "$new_path" ]; then echo -e "\\033[31m${new_path}\\033[0m"; cd "$new_path";else false; fi }

#Aliases
alias pi="/Users/kevinlin/code/pi/dist/patterninsight/application/bin/pi"

#Constants
export PATH=${HOME}/bin:/System/Library/Java/JavaVirtualMachines/1.6.0.jdk/Contents/Home/bin:$PATH #pi-code pre-req
export PATH=/usr/bin/:$PATH	    #necessary
export PATH=/opt/local/bin:$PATH    #port
export PATH=~/Dropbox/bin:$PATH	    #custom scripts
export PATH=/opt/local/Library/Frameworks/Python.framework/Versions/2.7/bin:$PATH
export PATH=~/Dropbox/asgard/bin/:$PATH

export HOME=/Users/kevinlin/
export PYTHONPATH=/Users/kevinlin/Dropbox/projects/:$PYTHONPATH
export PYTHONPATH=/opt/local/bin/:$PYTHONPATH
#Projects
export PYTHONPATH=/Users/kevinlin/Dropbox/asgard/pybin:$PYTHONPATH
export PYTHONPATH=~/Dropbox/asgard/pybin/pylibs/data_structurers:$PYTHONPATH

#django mingus
export PYTHONPATH=/Users/kevinlin/Test/t_mingus/django-mingus:$PYTHONPATH
export DJANGO_SETTINGS_MODULE=mingus.settings
#Temp

#Functions
#---------
function go () {
cd $1
ls
}

source ~/Dropbox/asgard/dotfiles/git/aliases.sh
source ~/Dropbox/asgard/dotfiles/bash/settings.rc
