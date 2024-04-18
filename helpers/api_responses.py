from fastapi.responses import JSONResponse
from fastapi import HTTPException

"""
Here we define all the API responses to be used in the application.
"""

def success_response(data):
    return JSONResponse(
        status_code=200, 
        content=data
        )

def not_found_response(detail="Not Found"):
    return HTTPException(
        status_code=404, 
        detail=detail
        )

def internal_server_error_response(detail="Internal Server Error"):
    return HTTPException(
        status_code=500, 
        detail=detail
        )

def bad_request_response(detail="Bad Request"):
    return HTTPException(
        status_code=400, 
        detail=detail
        )

def unauthorized_response(detail="Unauthorized"):
    return HTTPException(
        status_code=401, 
        detail=detail
        )

def forbidden_response(detail="Forbidden"):
    return HTTPException(
        status_code=403, 
        detail=detail
        )

def conflict_response(detail="Conflict"):
    return HTTPException(
        status_code=409, 
        detail=detail
        )

def too_many_requests_response(detail="Too Many Requests"):
    return HTTPException(
        status_code=429, 
        detail=detail
        )

def service_unavailable_response(detail="Service Unavailable"):
    return HTTPException(
        status_code=503, 
        detail=detail
        )