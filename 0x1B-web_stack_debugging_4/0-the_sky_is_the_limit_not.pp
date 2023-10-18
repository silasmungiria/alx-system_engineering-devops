# 0-the_sky_is_the_limit_not.pp

# Define an Exec resource to change the request limit in Nginx configuration.
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
  onlyif  => '/bin/grep -q "15" /etc/default/nginx',
  notify  => Exec['nginx-restart'],
}

# Define an Exec resource to restart Nginx.
exec { 'nginx-restart':
  command => 'service nginx restart',
  path    => '/etc/init.d/',
  refreshonly => true,
}

# Define a service resource for Nginx.
service { 'nginx':
  ensure => running,
}

# Notify the Exec resource to run if the service changes.
Service['nginx'] -> Exec['fix--for-nginx']
