# 2-puppet_custom_http_response_header.pp

# Update package list and install Nginx
package { 'nginx':
  ensure => 'installed',
}

# Create default page
file { '/var/www/html/index.nginx-debian.html':
  content => 'Hello World!',
}

# Create custom 404 page
file { '/usr/share/nginx/html/custom_404.html':
  content => "Ceci n'est pas une page",
}

# Configure Nginx
file { '/etc/nginx/sites-available/default':
  content => template('nginx/default.erb'),
}

# Add custom header to Nginx
file { '/etc/nginx/conf.d/custom_headers.conf':
  content => "add_header X-Served-By 91903-web-$::hostname;",
}

# Start Nginx
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => [Package['nginx'], File['/var/www/html/index.nginx-debian.html'], File['/usr/share/nginx/html/custom_404.html'], File['/etc/nginx/sites-available/default'], File['/etc/nginx/conf.d/custom_headers.conf']],
}
