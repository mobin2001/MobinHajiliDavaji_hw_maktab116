#!/bin/bash

todo_file="todo.txt"
done_file="done.txt"
deleted_file="deleted.txt"
fasele="________________________________________"
scope="${20 * "_"}"
#menu
menu() {
    echo "$fasele"
    printf "\n"
    echo "1. add new task"
    echo "2. show unfinished tasks"
    echo "3. mark task as done"
    echo "4. show completed tasks"
    echo "5. delete tasks"
    echo "6. show deleted tasks"
    echo "7. search tasks"
    echo "8. exit"
    echo "$fasele"
    printf "\n"
}

#add new tasks
add() {
    read -p "enter new task: " task
    read -p "priority from 1 to 3" priority
    read -p "enter date as yyyy-MM-DD" date
    read -p "time format: Hour:MIN" time
    
    echo "$priority | $date | $time | $task" >> $todo_file

    echo "task added successfully"
}

show_tasks() {
    if [[ -f "$1" ]]; then
        cat "$1"
    else
        echo "file $1 does not exist!"
    fi
}


show_deleted() {
    
    if [[ -f "$deleted_file" ]]; then
        cat "$deleted_file"
    else
        echo "file $deleted_file does not exist!"
    fi
}

mark_done(){
    read -p "enter the number of the completed task: " number
    
    sed -n "${number}p" $todo_file >> $done_file
    sed -i "${number}d" $todo_file
    echo "task is marked as done"
} 

delete_task() {
    read -p "enter task number to delete: " number
    
    sed -n "${number}p" $todo_file >> $deleted_file
    sed -i "${number}d" $todo_file
    echo "task deleted."
}

search_tasks() {
    read -p "enter what you are looking for" search_term
    
    echo "results in unfinished tasks: "
    grep "$search_term" $todo_file
    echo "results in completed tasks: "
    grep "$search_term" $done_file
    echo "results in deleted tasks: "
    grep "$search_term" $deleted_file
}

#main
while true; do
    menu
    read -p "please select from options: " choice
    
    case $choice in 
        1) add;;
        2) show_tasks $todo_file;;
        3) mark_done;;
        4) show_tasks $done_file;;
        5) delete_task;;
        6) show_deleted;;
        7) search_tasks;;
        8) exit 0;;
        *) echo "invalid option";;
    esac
done
