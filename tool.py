import re
from datetime import datetime
import logging
from logging.config import dictConfig
from logger import LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger("file_logger")

def validate_username(username):
    '''
    檢查創建的帳號名稱格式
    '''

    if len(username) < 3 or len(username) > 32:
        logger.warning("Username must have minimum 3 characters and maximum 32 characters in length")
        return False
    return True

def validate_password(password):
    '''
    檢查創建的密碼格式
    '''
    
    if len(password) < 8 or len(password) > 32:
        logger.warning("Password must have minimum 8 characters and maximum 32 characters in length")
        return False
    if not re.search(r'[A-Z]', password):
        logger.warning("Password must contain at least 1 uppercase letter")
        return False
    if not re.search(r'[a-z]', password):
        logger.warning("Password must contain at least 1 lowercase letter")
        return False
    if not re.search(r'\d', password):
        logger.warning("Password must contain at least 1 number")
        return False
    return True

def is_account_locked(accounts_lock, username):
    '''
    檢查帳戶是否被鎖定
    '''

    if username in accounts_lock and accounts_lock[username][0] >= 5:
        if datetime.now() < accounts_lock[username][1]:
            logger.warning("Account is locked")
            return True
        else:
            del accounts_lock[username]
    return False