from flask import jsonify

class APIResponse:
    @staticmethod
    def success(message='', data=None, status_code=None):
        response = {
            'success': True,
            'message': message,
            'data': data
        }
        return jsonify(response), status_code

    @staticmethod
    def error(message='', error=None, status_code=400):
        response = {
            'success': False,
            'message': message,
            'error': error
        }
        return jsonify(response), status_code
