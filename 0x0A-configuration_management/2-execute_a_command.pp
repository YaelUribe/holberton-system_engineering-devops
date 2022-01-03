# Puppet manifest to execute a command

exec { 'killmenow':
    path     => '/usr/bin:/bin/',
    command  => 'pkill killmenow',
    resource => 'shell',
}
