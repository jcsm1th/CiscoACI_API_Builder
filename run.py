from app import app
# If you need to make the application visible outside, change the
# ip address to 0.0.0.0. You can also change the port that
# the application will be listening.


app.run(host='0.0.0.0', debug=True, port=5007)
