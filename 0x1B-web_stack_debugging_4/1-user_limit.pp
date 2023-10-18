# 1-user_limit.pp

# Define a custom fact to check if the limits are already set.
Facter.add('holberton_limits_set') do
  setcode do
    File.readlines('/etc/security/limits.conf').grep(/holberton/).any?
  end
end

# Define a class for managing user limits.
class user_limits {
  if $facts['holberton_limits_set'] == false {
    exec { 'fix_limit_holberton_user':
      command => 'echo "holberton hard nofile 10000\nholberton soft nofile 20000" >> /etc/security/limits.conf',
      path    => '/usr/local/bin:/bin',
    }
  }
}

# Apply user_limits class only if the limits need to be set.
if $facts['holberton_limits_set'] == false {
  include user_limits
}
