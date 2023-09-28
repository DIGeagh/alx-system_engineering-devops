# Puppet manifest to install Flask version 2.1.0 using pip3
exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  path    => ['/usr/bin'],
  creates => '/usr/local/bin/flask', # Adjust the path if needed
}
