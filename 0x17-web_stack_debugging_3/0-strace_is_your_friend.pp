# Puppet manifest to fix a bug in wp-settings.php

# Define an exec resource to fix the PHP extension issue
exec { 'fix_php_extension_issue':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => '/usr/local/bin:/bin',
}
