bind = "0.0.0.0:8080"
workers = 2

# to run on Digital Ocean
# gunicorn --worker-tmp-dir /dev/shm app:app 