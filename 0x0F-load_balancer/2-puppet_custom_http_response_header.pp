exec { 'update_package_repository':
  command => 'sudo apt-get -y update',
  path    => ['/usr/bin', '/bin'],
  before  => Exec['install_nginx'],
}

exec { 'install_nginx':
  command => 'sudo apt-get -y install nginx',
  path    => ['/usr/bin', '/bin'],
  before  => Exec['configure_nginx_header'],
}

$hostname = $::hostname

exec { 'configure_nginx_header':
  command     => "sudo sed -i 's/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\\n\\tadd_header X-Served-By \"$hostname\";/' /etc/nginx/nginx.conf",
  path        => ['/usr/bin', '/bin'],
  refreshonly => true,
  subscribe   => File['/etc/nginx/nginx.conf'],
  notify      => Exec['restart_nginx'],
}

file { '/etc/nginx/nginx.conf':
  ensure  => present,
  require => Package['nginx'],
}

exec { 'restart_nginx':
  command     => 'sudo service nginx restart',
  path        => ['/usr/bin', '/bin'],
  refreshonly => true,
  subscribe   => Exec['configure_nginx_header'],
}
