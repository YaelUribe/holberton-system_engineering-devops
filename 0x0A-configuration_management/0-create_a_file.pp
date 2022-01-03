# puppet manifest to create a file
file { 'school':
    path    => '/tmp/school',
    mode    => '0744',
    content => 'I love puppet',
    owner   => 'www-data',
    group   => 'www-data',
}
