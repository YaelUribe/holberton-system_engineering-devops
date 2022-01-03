# Puppet manifest to create a file

file { 'school':
    ensure  => file,
    path    => '/tmp/school',
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0744',
    content => 'I love Puppet'
}
