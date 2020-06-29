import numpy as np
import pandas as pd
from logging import getLogger

TRAIN_DATA_PATH = '../input/train.csv'
TEST_DATA_PATH = '../input/test.csv'
logger = getLogger(__name__)

def load_train_data():
    logger.debug('enter')
    df = pd.read_csv(TRAIN_DATA_PATH)
    logger.debug('exit')
    return df

def load_test_data():
    logger.debug('enter')
    df = pd.read_csv(TEST_DATA_PATH)
    logger.debug('exit')
    return df