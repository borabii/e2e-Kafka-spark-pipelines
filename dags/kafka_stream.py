import uuid
from datetime import datetime
from airflow.decorators import dag, task
import json
from kafka import KafkaProducer
from airflow.operators.empty import EmptyOperator
import time
import logging
import requests


logger = logging.getLogger(__name__)

default_args = {
    'owner': 'rabii',
    'start_date': datetime(2024, 5, 25, 10, 00)
}

def get_data():

    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    res = res['results'][0]

    return res

def format_data(res):
    data = {}
    location = res['location']
    data['id'] = uuid.uuid4()
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['address'] = f"{str(location['street']['number'])} {location['street']['name']}, " \
                      f"{location['city']}, {location['state']}, {location['country']}"
    data['post_code'] = location['postcode']
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['registered_date'] = res['registered']['date']
    data['phone'] = res['phone']
    data['picture'] = res['picture']['medium']

    return data

    
@dag(start_date=datetime(2024, 5, 25, 10, 00),
     schedule=None,
     catchup=False)

def straming_Kafka():
    start = EmptyOperator(
        task_id='start'
    )
    end = EmptyOperator(
        task_id='end'
    )
    @task()
    def stream_data_from_api():
        producer = KafkaProducer(bootstrap_servers='localhost:29092')
        curr_time = time.time()

        while True:
            if time.time() > curr_time + 60: #1 minute
                break
            try:
                logger.info('Start')
                res = get_data()  
                logger.info("data is uploded")  
                res = format_data(res)
                logger.info("data is transformed")

                producer.send('test', json.dumps(res).encode('utf-8'))
            except Exception as e:
                logging.error(f'An error occured: {e}')
                continue
    start >> stream_data_from_api() >> end


straming_Kafka()

