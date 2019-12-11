<html>
<h1>Project: Web Server</h1>
<p><strong>In this project we will understand what is the main role of a web server, what is a child process, why web servers usually have a parent process and child processes, and what are the main HTTP requests.</strong></p>
<body>
<li>Task 0: Write a Bash script that transfers a file from our client to a server.</li>
<li>Task 1: Web servers are the piece of software generating and serving HTML pages, let’s install one!</li>
<li>Task 2: Provide the domain name in your answer file.
<ul>
<li>Provide the domain name only (example: foobar.tech), no subdomain (example: www.foobar.tech)</li>
<li>Configure your DNS records with an A entry so that your root domain points to your web-01 IP address Warning: the propagation of your records can take time (~1-2 hours)</li>
<li>Go to your profile and enter your domain in the Project website url field</li>
</ul></li>
<li>Task 3: Configure your Nginx server so that /redirect_me is redirecting to another page.</li>
<li>Task 4: Configure your Nginx server to have a custom 404 page that contains the string Ceci n'est pas une page.</li>
<li>Advanced Task 1: Design a beautiful 404 page</li>
<li>Advanced Task 2: Time to practice configuring your server with Puppet! Just as you did before, we’d like you to install and configure an Nginx server using Puppet instead of Bash. To save time and effort, you should also include resources in your manifest to perform a 301 redirect when querying /redirect_me.</li>
</body>
<br>
<br>
<footer>Made by: <strong><a href="https://github.com/DanielBaquero28">Daniel Baquero</a></strong></footer>
</html>