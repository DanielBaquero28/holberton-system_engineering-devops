<html>
<h1>Project:Application Server</h1>
<p><strong>In this project we will about application servers, how they work and why are they used. (Gunicorn)</strong></p>
<body>
<li>Task 0: Let’s serve what you built for AirBnB clone v2 - Web framework on web-01. This task is an exercise in setting up your development environment, which is used for testing and debugging your code before deploying it to production.</li>
<li>Task 1: Now that you have your development environment set up, let’s get your production application server set up with Gunicorn on web-01, port 5000. You’ll need to install Gunicorn and any libraries required by your application. Your Flask application object will serve as a WSGI entry point into your application. This will be your production environment. As you can see we want the production and development of your application to use the same port, so the conditions for serving your dynamic content are the same in both environments.</li>
<li>Task 2: Building on your work in the previous tasks, configure Nginx to serve your page from the route /airbnb-onepage/</li>
<li>Task 3: Building on what you did in the previous tasks, let’s expand our web application by adding another service for Gunicorn to handle. In AirBnB_clone_v2/web_flask/6-number_odd_or_even, the route /number_odd_or_even/<int:n> should already be defined to render a page telling you whether an integer is odd or even. You’ll need to configure Nginx to proxy HTTP requests to the route /airbnb-dynamic/number_odd_or_even/(any integer) to a Gunicorn instance listening on port 5001. The key to this exercise is getting Nginx configured to proxy requests to processes listening on two different ports. You are not expected to keep your application server processes running. If you want to know how to run multiple instances of Gunicorn without having multiple terminals open, see tips below.</li>
<li>Task 4: Let’s serve what you built for AirBnB clone v3 - RESTful API on web-01.</li>
<li>Task 5: Let’s serve what you built for AirBnB clone - Web dynamic on web-01.</li>
</body>
<br>
<br>
<footer>Made by: <strong><a href="https://github.com/DanielBaquero28">Daniel Baquero</a></strong></footer>
</html>