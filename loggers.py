# import logging.config
# import os
# from doctest import debug
#
# from utils import BASE_DIR
#
# logging.config.fileConfig(os.path.join(BASE_DIR,'log_config.ini'))
#
# # Використання логера
# sample_logger = logging.getLogger('sampleLogger')
#
# # logger.debug('Це повідомлення рівня DEBUG')
# # logger.info('Це повідомлення рівня INFO')
#
# logger_from_file = logging.getLogger('logger_from_file')
# logger_from_file.setLevel(logging.DEBUG)
#
# #file handler settings
# error_file_handler = logging.FileHandler('error.log')
# error_file_handler.setLevel(logging.ERROR)
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# error_file_handler.setFormatter(formatter)
#
# #file handler settings for DEBUG
# debug_file_handler = logging.FileHandler('debug.log')
# debug_file_handler.setLevel(logging.DEBUG)
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# debug_file_handler.setFormatter(formatter)
#
#
# #steam handler settings
# steam_handler = logging.StreamHandler()
# steam_handler.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# steam_handler.setFormatter(formatter)
#
# logger_from_file.addHandler(error_file_handler)
# logger_from_file.addHandler(debug_file_handler)
# logger_from_file.addHandler(steam_handler)
