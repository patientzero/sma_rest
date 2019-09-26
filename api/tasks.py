from sma_rest.celery import app

import time

"""
Define here the tasks that should be performed asynchronously e.g. the classification tasks
"""


@app.task
def celery_test():
    print('CELERY TEST!')
    time.sleep(10)
    return "Good night!"


@app.task
def celery_test2(x, y):
    return x * y