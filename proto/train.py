from logging import getLogger, StreamHandler, Formatter, FileHandler

DIR = './result_tmp/'
logger = getLogger(__name__)



if __name__ == "__main__":
    log_fmt = Formatter('%(asctime)s %(name)s %(lineno)d [%(levelname)s][%(funName)s][%(message)s]')
    handler = StreamHandler()
    handler.setLevel('INFO')
    handler.setFormatter('log_fmt')
    logger.addHandler(handler)

    handler = FileHandler(DIR + 'train.py.log')
    handler.setLevel('DEBUG')
    handler.setFormatter(log_fmt)
    logger.addHandler(handler)

    logger.info('Start')
    