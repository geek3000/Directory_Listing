#how can we prevent Directory Listing vulnerability in a web server

To prevent Directory Listing vulnerability in a web server we should edit the configuration files of the web server.

Depending of the web server we can do this:

#for apache web server, 
 add this line in httpd.conf files,
'''<Directory /{YOUR DIRECTORY}>
 Options FollowSymLinks
 </Directory>'''
 
	or create a .htaccess file in directory and put this lines:
	'''Options -Indexes'''
	
#for Nginx Server,
	edit the configuration file nginx.conf, it can be found at /usr/local/nginx/conf, /etc/nginx or /usr/local/etc/nginx
	Modified, it would be something like,
	'''server {
        listen   80;
        server_name  domain.com www.domain.com;
        access_log  /var/...........................;
        root   /path/to/root;
        location / {
                index  index.php index.html index.htm;
        }
        location /somedir {
               autoindex off;
        }
 }'''
 The value off autoindex must be off