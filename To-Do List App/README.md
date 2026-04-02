# To-Do List App

A simple 'Python console app' to manage your daily tasks.  
This version 'saves tasks to a file', so your tasks remain even after closing the program.  

## Features 

Add Task – Add new tasks to your list  
View Tasks – Show all current tasks  
Delete Task – Remove tasks by number  
Persistent Storage – Tasks are saved in `tasks.txt` and loaded at start  

## How It Works 

1. When the program starts, it **loads tasks from `tasks.txt`** (if exists)  
2. Tasks are stored in a **Python list** during runtime  
3. Every time a task is added or deleted, the program **updates the file**  
4. Program runs in a **loop until user exits**  

## Installation & Running

1. Make sure you have Python 3.x installed  
2. Download `todo_list.py` to your computer  
3. Open terminal / command prompt and navigate to the file location  
4. Run:

```bash
python todo_list.py
