__author__ = "Deem Alowairdhi"
__email__ = "411214706@qu.edu.sa"

# # """
# # A getting started code that establish a flask app with some
# # predefined configuration. 

# # There is only one route which returns a simple text to indicate
# # the server is working. No malicious link or missing files handling. 
# # """

# # from flask import Flask

# # """
# # Creating an instance of Flask app: An instance of the Flask class 
# # is created and assigned to the variable app. 
# # The __name__ argument tells Flask to use the current module as 
# # the starting point when it needs to load associated resources.
# # """

# # app = Flask(__name__)

# # """
# # This is defining a function hello() which will run when someone accesses 
# # the root URL ("/") of your server. 
# # The @app.route("/") is a decorator that tells Flask to call the 
# # hello() function when the root URL is visited. 
# # The function simply returns a string which will be shown to the user.
# # """
# # @app.route("/")
# # def hello():
# #     return "IT492 docker demo!"

# # """
# # "If this script is being run directly (and not imported as a module), 
# # then do the following." 
# # In this case, it's starting the Flask app.

# # debug=True allows the server to show detailed error messages 
# # and automatically reload when you make changes to the code.

# # host='0.0.0.0' means the server is accessible from any IP address, 
# # not just localhost. This is especially useful if you're 
# # running this in a container like Docker, 
# # so you can access the server from outside the container.
# # """
# # if __name__ == "__main__":
# #     app.run(debug=True, host='0.0.0.0')





# # from flask import Flask, send_from_directory, abort
# # import configparser
# # import os

# # app = Flask(__name__)

# # # Load configuration from credentials.ini
# # config = configparser.ConfigParser()
# # config.read('credentials.ini')
# # DOCROOT = config['DEFAULT']['DOCROOT']


# # @app.route('/<path:filename>')
# # def serve_file(filename):
# #     # Check for prohibited symbols
# #     if '..' in filename or '//' in filename or '~' in filename:
# #         abort(403)  # Return a 403 Forbidden status

# #     # Construct full file path
# #     full_path = os.path.join(DOCROOT, filename)

# #     # Check for .html or .css and if file exists
# #     if (filename.endswith('.html') or filename.endswith('.css')) and os.path.exists(full_path):
# #         return send_from_directory(DOCROOT, filename)  # Serve the file from the DOCROOT directory

# #     # If file does not exist, return 404
# #     abort(404)


# # @app.errorhandler(404)
# # def page_not_found(error):
# #     return send_from_directory(DOCROOT, '404.html'), 404


# # @app.errorhandler(403)
# # def forbidden_request(error):
# #     return send_from_directory(DOCROOT, '403.html'), 403


# # if __name__ == "__main__":
# #     PORT = int(config['DEFAULT']['PORT'])
# #     app.run(debug=True, host='0.0.0.0', port=PORT)




# # from flask import Flask, send_from_directory, abort, request
# # import configparser
# # import os

# # app = Flask(__name__)

# # # Load configuration from credentials.ini
# # config = configparser.ConfigParser()
# # config.read('credentials.ini')
# # DOCROOT = config['DEFAULT']['DOCROOT']

# # @app.before_request
# # def check_forbidden_symbols():
# #     raw_url = request.environ.get('REQUEST_URI')
# #     if any(symbol in raw_url for symbol in ['..', '//', '~']):
# #         abort(403)  # Return a 403 Forbidden status

# # @app.route('/<path:filename>')
# # def serve_file(filename):
# #     # Construct full file path
# #     full_path = os.path.join(DOCROOT, filename)

# #     # Check for .html or .css and if file exists
# #     if (filename.endswith('.html') or filename.endswith('.css')) and os.path.exists(full_path):
# #         return send_from_directory(DOCROOT, filename)  # Serve the file from the DOCROOT directory

# #     # If file does not exist, return 404
# #     abort(404)

# # @app.errorhandler(404)
# # def page_not_found(error):
# #     return send_from_directory(DOCROOT, '404.html'), 404

# # @app.errorhandler(403)
# # def forbidden_request(error):
# #     return send_from_directory(DOCROOT, '403.html'), 403

# # if __name__ == "__main__":
# #     PORT = int(config['DEFAULT']['PORT'])
# #     app.run(debug=True, host='0.0.0.0', port=PORT)



# from flask import Flask, send_from_directory, abort, request
# import configparser
# import os

# app = Flask(__name__)

# # Load configuration from credentials.ini
# config = configparser.ConfigParser()
# config.read('credentials.ini')
# DOCROOT = config['DEFAULT']['DOCROOT']

# @app.before_request
# def check_forbidden_symbols():
#     raw_url = request.path
#     if any(forbidden in raw_url for forbidden in ['..', '//', '~']):
#         abort(403)  # Return a 403 Forbidden status

# @app.route('/<path:filename>')
# def serve_file(filename):
#     # Construct full file path
#     full_path = os.path.join(DOCROOT, filename)

#     # Check for .html or .css and if the file exists
#     if (filename.endswith('.html') or filename.endswith('.css')) and os.path.exists(full_path):
#         return send_from_directory(DOCROOT, filename)  # Serve the file from the DOCROOT directory

#     # If file does not exist, return 404
#     abort(404)

# @app.errorhandler(404)
# def page_not_found(error):
#     return send_from_directory(DOCROOT, '404.html'), 404

# @app.errorhandler(403)
# def forbidden_request(error):
#     return send_from_directory(DOCROOT, '403.html'), 403

# if __name__ == "__main__":
#     PORT = int(config['DEFAULT']['PORT'])
#     app.run(debug=True, host='0.0.0.0', port=PORT)

from flask import Flask, send_from_directory, abort, request
import configparser
import os
import logging

# Initialize logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Load configuration from credentials.ini
config = configparser.ConfigParser()
config.read('credentials.ini')
DOCROOT = config['DEFAULT']['DOCROOT']
logger.info("Configuration loaded from credentials.ini")

@app.before_request
def check_forbidden_symbols():
    raw_url = request.path
    if any(forbidden in raw_url for forbidden in ['..', '//', '~']):
        logger.warning(f"Detected forbidden symbols in the URL: {raw_url}")
        abort(403)  # Return a 403 Forbidden status

@app.route('/<path:filename>')
def serve_file(filename):
    # Construct full file path
    full_path = os.path.join(DOCROOT, filename)
    logger.info(f"Serving file: {filename}")

    # Check for .html or .css and if the file exists
    if (filename.endswith('.html') or filename.endswith('.css')) and os.path.exists(full_path):
        return send_from_directory(DOCROOT, filename)  # Serve the file from the DOCROOT directory

    logger.warning(f"File not found: {filename}")
    # If file does not exist, return 404
    abort(404)

@app.errorhandler(404)
def page_not_found(error):
    logger.error("404 Page Not Found Error")
    return send_from_directory(DOCROOT, '404.html'), 404

@app.errorhandler(403)
def forbidden_request(error):
    logger.error("403 Forbidden Request Error")
    return send_from_directory(DOCROOT, '403.html'), 403

if __name__ == "__main__":
    PORT = int(config['DEFAULT']['PORT'])
    logger.info(f"Starting Flask app on port {PORT}")
    app.run(debug=True, host='0.0.0.0', port=PORT)
