# creates a file in /tmp
# The file (School) has permissions 0744, belonging to the user and group
# www-data.

file { '/tmp/school':
ensure  => present,
content =>'I love Puppet',
mode    => '0744',
owner   => 'www-data',
group   => 'www-data',
}
