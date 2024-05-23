from celery import Celery
x = 1
y = 5
app = Celery('example', broker='your_broker_url_here')

@app.task
def add(x, y):
    return x + y

print(add(x,y))
