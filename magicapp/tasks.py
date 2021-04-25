from celery.decorators import task

@task
def hello():
    print("\n\nYo Yo\n\n")