import logging
import os
import time

def get_logger(name="appium"):
    # 日志文件
    log_dir = os.path.join(os.getcwd(), "logs")
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"{time.strftime('%Y%m%dy')}.log")
    logger = logging.getLogger(name)
    if not logger.handlers:
        fh = logging.FileHandler(log_file,encoding='utf-8')
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    logger.setLevel(logging.INFO)
    return logger

logger = get_logger()