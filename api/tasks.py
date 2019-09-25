from sma_rest.celery import app


@app.task
def celery_test():
    print('CELERY TEST!')
