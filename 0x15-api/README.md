<html>
<h1>Project: API</h1>
<p><strong>In this project we will understand how to implement an API</strong></p>
<body>
<li>Task 0: Write a Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.
<br>
<ul>
<li>You must use urllib or requests module</li>
<li>The script must accept an integer as a parameter, which is the employee ID</li>
<li>The script must display on the standard output the employee TODO list progress with an exact format</li>
</ul>
</li>
<li>Task 1: Using what you did in the task #0, extend your Python script to export data in the CSV format
<ul>
<li>Records all tasks that are owned by this employee</li>
<li>Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"</li>
<li>File name must be: USER_ID.csv</li>
</ul>
</li>
<li>Task 2: Using what you did in the task #0, extend your Python script to export data in the JSON format.
<ul>
<li>Records all tasks that are owned by this employee</li>
<li>Format must be: { "USER_ID": [ {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}}, ... ]}</li>
<li>File name must be: USER_ID.json</li>
</ul>
</li>
<li>Task 3: Using what you did in the task #0, extend your Python script to export data in the JSON format.
<ul>
<li>Records all tasks from all employees</li>
<li>Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}</li>
<li>File name must be: todo_all_employees.json</li>
</ul>
</li>
</body>
<br>
<br>
<footer>Made by: <strong><a href="https://github.com/DanielBaquero28">Daniel Baquero</a></strong></footer>
</html>