# puppet manifest to install a package Puppet-lint

package { 'puppet-lint':
    ensure   => '2.5.0',
    provider => 'gem',
}
