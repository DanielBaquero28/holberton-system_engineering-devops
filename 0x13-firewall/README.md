<html>
<h1>Project: Firewall</h1>
<p><strong>In this project we will understand how to configure the rules of the firewall.</strong></p>
<body>
<li>Task 0: Pick one answer for every question.
<br>
What is a firewall?
<ol>
<li>A hardware security system</li>
<li>A hardware or software security system</li>
<li>A software security system</li>
</ol>
What are the 2 types of firewall:
<ol>
<li>Soft and hard firewall</li>
<li>Incoming and outgoing firewall</li>
<li>Network and host-based firewall</li>
</ol>
What is the main function of a firewall?
<ol>
<li>To filter incoming and outgoing network traffic</li>
<li>To filter incoming and outgoing TCP traffic</li>
<li>To filter outgoing traffic</li>
</ol>
</li>
<li>Task 1: Let’s install the ufw firewall and setup a few rules on web-01.
Requirements:
<ul>
<li>The requirements below must be applied to web-01 (feel free to do it on lb-01 and web-02, but it won’t be checked)</li>
<li>Configure ufw so that it blocks all incoming traffic, except the following TCP ports:
<ul>
<li>22 (SSH)</li>
<li>443 (HTTPS SSL)</li>
<li>80 (HTTP)</li>
</ul>
</li>
<li>Share the ufw commands that you used in your answer file</li>
</ul>
</li>
<li>Advanced Task 1: Requirements:
<ul>
<li>Configure web-01 so that its firewall redirects port 8080/TCP to port 80/TCP</li>
<li>Your answer file should be a copy of the ufw configuration file that you modified to make this happen</li>
</ul>
</li>
</body>
<br>
<br>
<footer>Made by: <strong><a href="https://github.com/DanielBaquero28">Daniel Baquero</a></strong></footer>
</html>
