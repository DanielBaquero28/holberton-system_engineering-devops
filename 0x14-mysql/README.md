<html>
<h1>Project: MySQL</h1>
<p><strong> In this project we'll learn how to create database replicas (master-slave replica)</strong></p>
<body>
<li>Task 0: First things first, let’s get MySQL installed on both your web-01 and web-02 servers.</li>
<li>Task 1: In order for us to verify that your servers are properly configured, we need you to create a user and password for both MySQL databases which will allow the checker access to them.</li>
<li>Task 2: In order for you to set up replication, you’ll need to have a database with at least one table and one row in your primary MySQL server (web-01) to replicate from.</li>
<li>Task 3: Before you get started with your primary-replica synchronization, you need one more thing in place. On your primary MySQL server (web-01), create a new user for the replica server.</li>
<li>Task 4:
<ul>
<li>MySQL primary must be hosted on web-01 - do not use the bind-address, just comment out this parameter</li>
<li>MySQL replica must be hosted on web-02</li>
<li>Provide your MySQL primary configuration as answer file(my.cnf or mysqld.cnf) with the name 4-mysql_configuration_primary</li>
<li>Provide your MySQL replica configuration as an answer file with the name 4-mysql_configuration_replica</li>
</ul>
</li>
<li>Task 5: Write a Bash script that generates a MySQL dump and creates a compressed archive out of it.</li>
</body>
<br>
<br>
<footer>Made by: <strong><a href="https://github.com/DanielBaquero28">Daniel Baquero</a></strong></footer>
</html>