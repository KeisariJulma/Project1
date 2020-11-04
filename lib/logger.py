import logging
from datetime import datetime
from lib.config import load_config
config = load_config()
logging.basicConfig(level=int(config['Log']['Loggin Level']),
                    format='%(asctime)s %(process)d %(filename)s %(levelname)s %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S',
                    filename='logs\\{:%Y-%m-%d-%H_%M_%S}.log'.format(datetime.now()),
                    filemode='a')
