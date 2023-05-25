# Website is a python package so the files inside it become a package
from website import create_app

app = create_app()

# Only can run web server from this file directly
if __name__ == '__main__':
    # Debug reruns the website
    app.run(debug = True)