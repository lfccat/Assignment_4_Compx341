import time

import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

def prime(num):
    isprime = True
    i = 2
    if num <= 1:
        isprime = False
    
 
    while i <= num:
        if num % i == 0 and i != num:
            isprime = False
            
            return isprime
        else:
            i+= 1
    return isprime


@app.route('/isPrime/<int:number>')
def primes(number):
    
    primer = prime(number)
    if primer == True:
        return '{} is prime. \n'.format(number)
    elif primer == False:
        return '{} is not prime. \n'.format(number)

    


@app.route('/hello')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)


