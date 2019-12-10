# Connecting to a sever via ssh without asking for a password
exec {'/etc/ssh/ssh_config':
     command    => '/bin/echo -e "IdentityFile ~/.ssh/holberton\n PasswordAuthentication no" >> /etc/ssh/ssh_config',
     path       => '/etc/ssh/ssh_config',
}
