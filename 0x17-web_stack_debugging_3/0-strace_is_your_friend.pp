# Solving an 500 error by using a shell tool (sed) to replace all of the occurences in wp-settings.php of phpp to php
exec { 'change':
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  provider => 'shell'
}
