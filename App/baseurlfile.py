# base_url='https://gptsenderapp.onrender.com/'
# base_url='http://143.198.224.47:8000/'
base_url='http://localhost:8000/'
# base_url='https://gptsender.ddns.net/'
# databasename=gptsenderdb
# CREATE USER kc WITH PASSWORD 'Gptsender2023!';GRANT ALL PRIVILEGES ON DATABASE gptsenderdb TO kc;
# mkdir ~/gptsender
# cd ~/gptsenderpython3 -m venv venv
# 
#
#
# [Unit]
# sudo nano /etc/nginx/sites-available/gptsender
# Description=gunicorn daemon
# Requires=gunicorn.socket
# After=network.target

# [Service]
# User=root
# Group=www-data
# WorkingDirectory=/root/gptsender
# ExecStart=/root/gptsender/venv/bin/gunicorn \
#           --access-logfile - \
#           --workers 3 \
#           --bind unix:/run/gunicorn.sock \
#           CoreRoot.wsgi:application
# sudo nano /etc/nginx/sites-available/gptsender
# sudo certbot --nginx -d gptsender.cfd -d www.gptsender.cfd
# server {
#     listen 80;
#     server_name gptsender.cfd www.gptsender.cfd;

#     location = /favicon.ico { access_log off; log_not_found off; }
#     location /static/ {
#         root /root/gptsender;
#     }

#     location / {
#         include proxy_params;
#         proxy_pass http://unix:/run/gunicorn.sock;
#     }
# }
# sudo ln -s /etc/nginx/sites-available/gptsender /etc/nginx/sites-enabled
# pyinstaller --name="gptsenderapp" --windowed loading_view.py