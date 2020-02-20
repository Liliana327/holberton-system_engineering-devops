# Strace is your friend

exec { 'replace':
    command => '/usr/bin/env sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php'
}
