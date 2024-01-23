# Project-2-Flask-Pageserver

## 1. Project Overview

`Project-2-Flask-Pageserver` demonstrates the capabilities of Docker and web frameworks. This project signifies a progression from earlier endeavors, focusing on the file-checking logic similar to the [first project](https://github.com/it492/project-1-pageserver-Deemowe/blob/main/README.md) but utilizing Flask.

## 2. Author Information

- **Name:** Deem Alowairdhi
- **QU ID:** 411214706
- **Email:** 411214706@qu.edu.sa

## 3. Objectives

- **Containerization**: Utilize `Docker` for dependency management, ensuring software consistency across different environments.
  
- **Web Frameworks**: Implement `Flask`, a micro web framework, for efficient web service handling.

## 4. Introduction to Docker

`Docker` provides a platform for developing, shipping, and executing applications within containers. These containers encapsulate an application along with its required components, ensuring it runs consistently across different environments.

## 5. Docker Terminology

- **Docker Image**: A standalone software package encompassing everything necessary to execute a software piece.

- **Docker Container**: An active instance of a `Docker image`, running in isolation unless explicitly permitted.

## 6. About Flask

`Flask` is a micro web framework, written in Python. It offers a seamless setup and rapid deployment, catering to both small and larger applications.

## 7. Project Structure

### File Descriptions

- `app.py`: The core application logic for the Flask server.
- `credentials.ini`: A configuration file template for defining settings, including author details, repository link, port settings, and document root.
- `Dockerfile`: Contains steps and commands to build the Docker container.
- `requirements.txt`: Enumerates Python dependencies for the Flask application.
- `.gitignore`: Denotes which files or directories Git should ignore.
- `403.html` & `404.html`: Custom error pages for forbidden access and not found responses, respectively.
- `trivia.html` & `trivia.css`: A sample web page and its associated styling
- `tests.sh`: A shell script designed to evaluate the web server's responses by sending HTTP requests to various URLs and contrasting these responses with expected results, resulting in either a "Pass" or "Fail" verdict.

### `app.py` Breakdown
The `app.py` serves as the backbone for this Flask application, governing how it handles incoming web requests, routes them, and responds. Here's a closer look at the components:

 
   ```python
   from flask import Flask, send_from_directory, abort, request
   ```
   This line imports required modules from Flask:
   - `Flask`: The core class that represents a Flask web application.
   - `send_from_directory`: A function to send files from a directory.
   - `abort`: A function to terminate a request with an error code.
   - `request`: A global object in Flask that contains details of the current request.

 
   ```python
   import configparser
   ```
   Imports the `configparser` module, which allows reading and writing of .ini files.

 
   ```python
   import os
   ```
   Imports the `os` module which provides functions for interacting with the operating system.

 
   ```python
   import logging
   ```
   Imports the `logging` module to handle logging.

 
   ```python
   # Initialize logging
   logging.basicConfig(level=logging.DEBUG)
   logger = logging.getLogger(__name__)
   ```
   Sets up logging:
   - `basicConfig`: Configures the logging to show DEBUG level messages and above.
   - `getLogger`: Retrieves or creates a logger instance with the name of the current module (`__name__`).

 
   ```python
   app = Flask(__name__)
   ```
   Creates a new Flask web application instance.

   ```python
   # Load configuration from credentials.ini
   config = configparser.ConfigParser()
   config.read('credentials.ini')
   DOCROOT = config['DEFAULT']['DOCROOT']
   logger.info("Configuration loaded from credentials.ini")
   ```
   Uses `configparser` to read configuration from the 'credentials.ini' file and sets the `DOCROOT` variable based on the value specified in that file. It then logs that the configuration has been loaded.

   ```python
   @app.before_request
   def check_forbidden_symbols():
       raw_url = request.path
       if any(forbidden in raw_url for forbidden in ['..', '//', '~']):
           logger.warning(f"Detected forbidden symbols in the URL: {raw_url}")
           abort(403)
   ```
   A Flask `before_request` decorator, which runs before each request. This function checks if the URL contains any forbidden symbols (like `..`, `//`, or `~`). If it does, a warning is logged and a 403 Forbidden status is returned.


   ```python
   @app.route('/<path:filename>')
   def serve_file(filename):
       full_path = os.path.join(DOCROOT, filename)
       logger.info(f"Serving file: {filename}")
       if (filename.endswith('.html') or filename.endswith('.css')) and os.path.exists(full_path):
           return send_from_directory(DOCROOT, filename)
       logger.warning(f"File not found: {filename}")
       abort(404)
   ```
   Defines a Flask route for any URL that matches the pattern `/<path:filename>`. This function will serve HTML and CSS files from the `DOCROOT` directory if they exist. If the file doesn't exist, it logs a warning and returns a 404 status.


   ```python
   @app.errorhandler(404)
   def page_not_found(error):
       logger.error("404 Page Not Found Error")
       return send_from_directory(DOCROOT, '404.html'), 404
   ```
   Specifies a custom error handler for the 404 error. Logs the error and serves a custom 404.html page from the `DOCROOT` directory.

   ```python
   @app.errorhandler(403)
   def forbidden_request(error):
       logger.error("403 Forbidden Request Error")
       return send_from_directory(DOCROOT, '403.html'), 403
   ```
   Specifies a custom error handler for the 403 error. Logs the error and serves a custom 403.html page from the `DOCROOT` directory.


   ```python
   if __name__ == "__main__":
       PORT = int(config['DEFAULT']['PORT'])
       logger.info(f"Starting Flask app on port {PORT}")
       app.run(debug=True, host='0.0.0.0', port=PORT)
   ```
   This block of code runs only if this script is executed directly (not imported as a module). It reads the port from the configuration file, logs the start of the Flask app, and then runs the Flask application on the specified port, listening on all available network interfaces (`0.0.0.0`).


## 8. Building and Running with Docker

To comprehend and successfully run the Flask application using Docker, follow the steps and understand the concepts below:

### Exploring the Repository

1. Navigate to the **web** folder within the repository.
2. Carefully read through each line in the `Dockerfile` to understand its purpose and significance. 
3. Familiarize yourself with the simple Flask app provided.

### Building the Docker Image

Execute the following command to build the Docker image:

```bash
docker build -t it492-flask-image .
```

Breaking down the command:
- **-t**: Specifies a name and optionally a tag in the 'name:tag' format. In essence, it's naming the image.
- **it492-flask-image**: This is the name you're giving the Docker image.
- **.**: The dot at the end of the command refers to the current directory. Docker will look for the `Dockerfile` in the current directory to build the image.

### Running the Docker Container

To run the Docker container, use:

```bash
docker run -d -p 1100:1100 it492-flask-image
```

Breaking down the command:
- **-d**: Runs the container in detached mode, meaning the container runs in the background.
- **-p 1100:1100**: Maps the port 1100 of the container to port 1100 on the host machine.
- **it492-flask-image**: Specifies the image name to create the container from.

By following these steps, you'll have the Flask app running within a Docker container.

## 9. Testing

For testing the pageserver, please refer to the `Readme.md` of [project-1-pageserver-Deemowe](https://github.com/it492/project-1-pageserver-Deemowe/blob/main/README.md). You have two primary methods for testing:

1. **Manual Testing**:
   - Use a web browser to navigate through the application.
   - Alternatively, employ terminal commands such as `curl`.

2. **Automated Testing**:
   - Utilize the `tests.sh` script. 
   ```bash
   $ ./tests.sh localhost:portnumber
   ```
   This script will assess the application and provide feedback, indicating either a "pass" or "fail" outcome based on the tests conducted.