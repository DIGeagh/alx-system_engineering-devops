# Puppet manifest to install puppet-lint version 2.5.0
exec { 'install_puppet_lint':
  command => '/usr/bin/apt-get install -y puppet-lint=2.5.0',
  path    => '/usr/bin',
  creates => '/usr/bin/puppet-lint',
  require => Package['ruby'],
}
