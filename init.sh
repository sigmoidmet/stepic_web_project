sudo cp /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test2.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo gunicorn -b 0.0.0.0:8080 /home/box/web/hello.py:app &
