import os
import pytest
import sys
import pathlib
from unittest.mock import patch
from lesson_11.homework_11 import log_event

from lesson_11.core.function_asserts.function_asserts import read_file, assert_true, assert_file_exists
sys.path.append(str(pathlib.Path(__file__).parent.parent.parent))
from lesson_11.homework_11  import log_event
from utils import BASE_DIR

FILE_PATH = os.path.join(BASE_DIR, 'login_system.log')

@pytest.mark.log_event
def test_log_event_writes_file():
    """Log file should be created upon calling log_event function"""
    log_event('test', 'success')
    assert_file_exists(FILE_PATH)

@pytest.mark.parametrize('username,password', [
    ('admin', 'success'),
    ('user', 'expired'),
    ('', 'test'),
    ('', 'fail')
])
@pytest.mark.log_event
def test_log_event_returns_correct_message(username, password):
    """Log_event should return correct message including correct username and password"""
    log_event(username, password)
    message = read_file(FILE_PATH)
    assert_true(username, password, message)

@pytest.mark.parametrize('username,password,method', [
    ('admin', 'success', 'info'),
    ('user', 'expired', 'warning'),
    ('test', 'test', 'error')
])
@pytest.mark.log_event
def test_log_event_method(username, password, method):
    """Log_event should trigger correct log level type"""
    # 1️Replace "logging.getLogger" inside your module with a mock
    with patch("lesson_11.homework_11.logging.getLogger") as mock_get_logger:
        # 2️When your code calls logging.getLogger(), return this fake logger
        mock_logger = mock_get_logger.return_value
        # 3️ Call your real function
        log_event(username, password)
        getattr(mock_logger, method).assert_called_once()
        # Optionally ensure others were not called
        for other_method in ["info", "warning", "error"]:
            if other_method != method:
                getattr(mock_logger, other_method).assert_not_called()



