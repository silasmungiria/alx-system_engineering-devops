#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.

# Check if Nginx is already installed
if ! command -v nginx &> /dev/null
then
    apt-get update
    apt-get install -y nginx
fi

# Create directories if they don't exist
directories=("/data/web_static/releases/test/" "/data/web_static/shared/")
for dir in "${directories[@]}"
do
    mkdir -p "$dir"
done

# Create fake HTML file
echo "Holberton School" > /data/web_static/releases/test/index.html

# Create symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# Set ownership and group recursively
chown -R ubuntu /data/
chgrp -R ubuntu /data/

# Update Nginx configuration
nginx_config="/etc/nginx/sites-available/web_static"
if [ ! -f "$nginx_config" ]; then
    printf %s "server {
        listen 80 default_server;
        listen [::]:80 default_server;
        add_header X-Served-By $HOSTNAME;
        root   /var/www/html;
        index  index.html index.htm;
        location /hbnb_static {
            alias /data/web_static/current;
            index index.html index.htm;
        }
        error_page 404 /404.html;
        location /404 {
          root /var/www/html;
          internal;
        }
    }" > "$nginx_config"

    # Create symbolic link to enable the site
    ln -s "$nginx_config" "/etc/nginx/sites-enabled/"
fi

# Restart Nginx service
service nginx restart

# Exit successfully
exit 0
