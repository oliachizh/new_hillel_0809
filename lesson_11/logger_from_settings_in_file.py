import logging

# Створення конфігурації
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s - %(levelname)s - %(message)s',
#                     handlers=[
#                         logging.StreamHandler(),  # Виведення в консоль
#                         logging.FileHandler('example.log')  # Запис у файл
#                     ])

# logger_from_file = logging.getLogger('logger_from_file')
# logger_from_file.setLevel(logging.DEBUG)
#
# #file handler settings
# file_handler = logging.FileHandler('error.log')
# file_handler.setLevel(logging.ERROR)
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# file_handler.setFormatter(formatter)
#
# #file handler settings for DEBUG
# file_handler = logging.FileHandler('debug.log')
# file_handler.setLevel(logging.DEBUG)
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# file_handler.setFormatter(formatter)
#
#
# #steam handler settings
# file_handler = logging.StreamHandler()
# file_handler.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# file_handler.setFormatter(formatter)
#
# logger_from_file.addHandler(file_handler)


# # Використання логера
# logger = logging.getLogger(__name__)
#
# logger.debug('Це повідомлення рівня DEBUG')
# logger.info('Це повідомлення рівня INFO')