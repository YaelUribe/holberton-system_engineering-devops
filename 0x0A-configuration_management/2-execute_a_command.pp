# Puppet manifest to execute a command

exec { 'killmenow':
    command  => 'pkill -f killmenow',
    path     => '/usr/bin/:/bin/:/usr/local/bin/',
    resource => 'shell',
}
