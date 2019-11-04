
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
gunicorn --bind=0.0.0.0:8000 --workers=2 --timeout=15 --log-level=debug /home/box/web/ask ask.wsgi:application
