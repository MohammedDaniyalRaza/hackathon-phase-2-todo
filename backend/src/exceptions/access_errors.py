from fastapi import HTTPException, status
from src.logging.audit import AuditLog

def handle_unauthorized_access(user_id: str, resource: str, action: str, ip_address: str = None):
    """
    Handle unauthorized access attempts by logging them and raising an HTTPException
    """
    # Log the unauthorized access attempt
    AuditLog.log_access_attempt(
        user_id=user_id,
        resource=resource,
        action=action,
        success=False,
        ip_address=ip_address
    )
    
    # Raise the appropriate HTTP exception
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="You do not have permission to access this resource"
    )

def handle_resource_not_found(resource: str, resource_id: str):
    """
    Handle resource not found errors
    """
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"{resource.capitalize()} with ID {resource_id} not found"
    )

def handle_validation_error(error_msg: str):
    """
    Handle validation errors
    """
    raise HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail=error_msg
    )