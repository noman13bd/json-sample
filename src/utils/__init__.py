from http import HTTPStatus
from typing import Union, List, Dict, Any
from flask import jsonify, make_response

class ResponseGenerator:
    @staticmethod
    def generate_response(data: Union[str, List[Any], Dict[str, Any]], code: int, error: bool = False):
        if error:
            response_data = {
                "error": {
                    "mssg": data
                }
            }
        else:
            response_data = {
                "result": data
            }
        
        return make_response(jsonify(response_data), code)
    
    @staticmethod
    def error_response(mssg: str, code: int):
        return ResponseGenerator.generate_response(mssg, code, True)
    
    #@staticmethod
    def json_data_expected(mssg: str = "JSON data expected!", code: int = HTTPStatus.BAD_REQUEST):
        return ResponseGenerator.error_response(mssg, code)
    
    #@staticmethod
    def user_login_failed(mssg: str = "Either email or password does not match!", code: int = HTTPStatus.UNAUTHORIZED):
        return ResponseGenerator.error_response(mssg, code)
    