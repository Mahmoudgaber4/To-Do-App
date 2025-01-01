# To-Do App: 


## Phase One
### 1.Module Name:
- todo_management

### 2.Model:
- todo.task with:
- Task Name
- Assigned To
- Due Date
- State (New, In Progress, Completed)

### 3.Menu:
- To-Do > All Tasks

### 4.Views:
- Tree View: List tasks with Task Name, Assigned To, Due Date, and State.
- Form View: Edit task details (validate due date).
- Search View:
  - Search By: Task Name, Assigned To 
  - Filter: State 
  - Group By: State, Assigned To, Due Date

### 5.Extras:
- Add Chatter for updates.

## Phase Two
### 1.Lines: 
- Add estimated_time, log task_id, description, date, time, and ensure total time ≤ estimated.
### 2.Archiving: 
- Add archive/unarchive functionality for records.
### 3.Close Tickets: 
- Add a server action to mark tickets as closed.
### 4.Alerts & Highlighting: 
- Auto-flag overdue due_date tasks and color them red in tree view if new or in_progress.
### 5.Reports: 
- Implement a report action for tasks.