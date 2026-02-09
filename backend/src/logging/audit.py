import logging
from datetime import datetime
from typing import Optional
import json

# Set up logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class AuditLog:
    @staticmethod
    def log_access_attempt(user_id: str, resource: str, action: str, success: bool, ip_address: Optional[str] = None):
        """
        Log an access attempt to a resource
        """
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "user_id": user_id,
            "resource": resource,
            "action": action,
            "success": success,
            "ip_address": ip_address
        }
        
        if success:
            logger.info(f"AUDIT_ACCESS_SUCCESS: {json.dumps(log_entry)}")
        else:
            logger.warning(f"AUDIT_ACCESS_FAILED: {json.dumps(log_entry)}")
    
    @staticmethod
    def log_authentication_event(user_id: str, event_type: str, ip_address: Optional[str] = None, details: Optional[dict] = None):
        """
        Log authentication events (login, logout, etc.)
        """
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "user_id": user_id,
            "event_type": event_type,
            "ip_address": ip_address,
            "details": details
        }
        
        logger.info(f"AUDIT_AUTH_EVENT: {json.dumps(log_entry)}")
    
    @staticmethod
    def log_security_event(event_type: str, severity: str, details: dict, ip_address: Optional[str] = None):
        """
        Log security-related events
        """
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "event_type": event_type,
            "severity": severity,
            "details": details,
            "ip_address": ip_address
        }
        
        if severity.lower() == 'high':
            logger.critical(f"SECURITY_ALERT: {json.dumps(log_entry)}")
        elif severity.lower() == 'medium':
            logger.error(f"SECURITY_EVENT: {json.dumps(log_entry)}")
        else:
            logger.warning(f"SECURITY_EVENT: {json.dumps(log_entry)}")