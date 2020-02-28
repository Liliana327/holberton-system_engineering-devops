# Sky is the limit, let's bring that limit higher
exec { 'replace':
    command => '/bin/sed -i "s/15/30000/g" /etc/default/nginx | service nginx restart'
}
