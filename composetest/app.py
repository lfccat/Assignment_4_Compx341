import time

import redis
from flask import Flask

app = Flask(__name__)
redisClient = redis.Redis(host='redis', port=6379)
numberList = "numbers"





def prime(num):
    isprime = True
    i = 2
    if num <= 1:
        isprime = False
        return isprime
    while i <= num:
        if num % i == 0 and i != num:
            isprime = False
            
            return isprime
        else:
            i+= 1
    return isprime

@app.route('/primesStored')
def store():
    retries = 5
    count = b''
    while True:
       try:
           for i in range(0, redisClient.llen(numberList)):
       
               count += redisClient.lindex(numberList, i)
               count += b' '
           return '{}\n'.format(str(count, 'utf-8'))
       except redis.exceptions.ConnectionError as exc:
           if retries == 0:
               raise exc
           retries -= 1
           times.sleep(0.5)


@app.route('/isPrime/<int:number>')
def primes(number):
    
    primer = prime(number)
    if primer == True:
        redisClient.lpush(numberList, number)
        
        
        return '{} is prime. \n'.format(number)
    elif primer == False:
        return '{} is not prime. \n'.format(number)


