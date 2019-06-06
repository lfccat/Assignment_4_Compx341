import time
import math
import redis
from flask import Flask

app = Flask(__name__)
redisClient = redis.Redis(host='redis', port=6379)
numberList = "numbers"

#no longer in use function
# @app.route('/clear')
# def clear():
#    redisClient.flushdb()
#   return 'Cleared redis \n'



def prime(num):
     
    if num <= 1:
        return False
    if num == 2:
        return True
    if num > 2 and num % 2 == 0:
        return False
    max_div = math.floor(math.sqrt(num))
    for i in range(3, 1 + max_div, 2):
        if num % i == 0:
            return False
            
    return True

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
    match = False
    primer = prime(number)
    num2 = str(number).encode()
    if primer == True:
        while True:
            try:
                for i in range(0, redisClient.llen(numberList)):
                    if redisClient.lindex(numberList, i) == num2:                   
                       match = True
                       break
                if match == False:
                    redisClient.lpush(numberList,number)
                return '{} is prime. \n'.format(number)            
            except redis.exceptions.ConnectionError as exc:
                if retries == 0:
                    raise exc
                retries -= 1
                times.sleep(0.5)
        
        
        
    elif primer == False:
        return '{} is not prime. \n'.format(number)






