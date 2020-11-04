from configobj import ConfigObj
from datetime import datetime
import logging
import sys

logging.basicConfig(level=20,
                    format='%(asctime)s %(process)d %(filename)s %(levelname)s %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S',
                    filename='logs\\{:%Y-%m-%d-%H_%M_%S}.log'.format(datetime.now()),
                    filemode='a')


def load_config():
    try:
        config = ConfigObj(infile='config\\config.ini',
                           raise_errors=True,
                           list_values=True,
                           create_empty=False,
                           file_error=True,
                           interpolation=True,
                           encoding='UTF-8',
                           write_empty_values=True)
        logging.info('Loaded config')
        return config
    except OSError as e:
        logging.error(e)
        sys.exit()
