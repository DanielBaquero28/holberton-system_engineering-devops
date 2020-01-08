<html>
<h1>Project: HTTPS-SSL</h1>
<p><strong>In this project we will learn about SSL certificates, how they're used, why do they exist and why are they so important when increasing security in our web servers.</strong></p>
<body>
<li>Task 0: What is HTTPS ?
<ol>
<li>A secure version of HTTP</li>
<li>A faster version of HTTP</li>
<li>A superior version of HTTP</li>
<ol>
<br>
Why do you need HTTPS?
<ol>
<li>To encrypt credit card and social security number information going between the client and the website servers</li>
<li>To encrypt all communication between the client and the website servers</li>
<li>To accelerate the communication between the client and the website servers</li>
<ol>
You want to setup HTTPS on your website, where shall you place the certificate?
<ol>
<li>In a secure location where nobody can access it</li>
<li>You can host it anywhere but you have to share the link to it on your website</li>
<li>On your website web server(s)</li>
<ol>
</li>
<li>Task 1: Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.</li>
<li>Task 2: “Terminating SSL on HAproxy” means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to its destination. Create a certificate using certbot and configure HAproxy to accept encrypted traffic for your subdomain www.</li>
<li>Advanced Task 1: A good habit is to enforce HTTPS traffic so that no unencrypted traffic is possible. Configure HAproxy to automatically redirect HTTP traffic to HTTPS.</li>
</body>
<br>
<br>
<footer>Made by: <strong><a href="https://github.com/DanielBaquero28">Daniel Baquero</a></strong></footer>
</html>