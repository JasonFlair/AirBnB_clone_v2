#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

# install nginx if its not installed
apt-get update
apt-get install -y nginx

# create necessary directories
mkdir /data/
mkdir /data/web_static/
mkdir /data/web_static/releases/
mkdir /data/web_static/shared/
mkdir /data/web_static/releases/test/
echo "hello jason" > /data/web_static/releases/test/index.html

# removes and and recreates symbolic link every time the script is ran
rm /data/web_static/current
ln -s /data/web_static/releases/test/ /data/web_static/current
# Give ownership of the /data/ folder to the ubuntu user AND group 
chown -R ubuntu:ubuntu /data/

# update the Nginx configuration to serve the content of /data/web_static/current/
echo -e "
server {
   listen 80 default_server;
   listen [::]:80 default_server;

   root /var/www/html;
   index index.html;
   location /hbnb_static {
      alias /data/web_static/current;
      index index.html index.htm;
   }
   location /redirect_me {
      return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
   }
   error_page 404 /404.html;
   location = /404.html{
      internal;
   }
}" > /etc/nginx/sites-available/default
nginx -s reload
