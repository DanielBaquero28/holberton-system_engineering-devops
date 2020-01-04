# Installs a Nginx server with custome HTTP header

exec {'updating':
     provider => shell,
     command  => 'sudo apt-get -y update',
     before   => Exec['installing Nginx'],
}

exec {'installing Nginx':
     provider => shell,
     command  => 'sudo apt-get -y install nginx',
     before   => Exec['adding header'],
}
exec {'adding header':
     provider    => shell,
     environment => ["HOST=${hostname}"],
     command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$HOST\";/" /etc/nginx/nginx.conf',
     before      => Exec['restarting Nginx'],
}

exec {'restarting Nginx':
     provider => shell,
     command  => 'sudo service nginx restart'
}
