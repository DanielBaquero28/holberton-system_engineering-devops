# Fixing error of 24: too many open files for the working processes; have to raise the limit

exec { 'change':
  command  => 'sudo sed -i "s/15/30000/" /etc/default/nginx',
  provider => 'shell',
  before   => Exec['restart'],
}

exec { 'restart':
  command  => 'sudo service nginx restart',
  provider => 'shell',
}
