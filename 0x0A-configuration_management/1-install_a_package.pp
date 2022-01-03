# puppet manifest to install a package Puppet-lint

package { 'puppet-lint':
    ensure   => '2.1.1',
    provider => 'gem',
}
