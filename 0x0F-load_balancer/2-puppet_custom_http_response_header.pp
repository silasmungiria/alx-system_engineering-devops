#!/usr/bin/puppet apply

package {'nginx':
  ensure => 'installed',
}

file {'/var/www/html/index.nginx-debian.html':
  content => 'Hello World!',
}

file {'/usr/share/nginx/html/custom_404.html':
  content => "Ceci n'est pas une page",
}

file {'/etc/nginx/sites-available/default':
  content => template('nginx/default.erb'),
}

file {'/etc/nginx/nginx.conf':
  content => template('nginx/nginx.conf.erb'),
}

service {'nginx':
  ensure  => 'running',
  enable  => true,
  require => [Package['nginx'], File['/var/www/html/index.nginx-debian.html'], File['/usr/share/nginx/html/custom_404.html'], File['/etc/nginx/sites-available/default'], File['/etc/nginx/nginx.conf']],
}

Facter.add('custom_served_by_header') do
  setcode do
    Facter::Core::Execution.execute('hostname')
  end
end

