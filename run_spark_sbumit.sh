#!/bin/bash

docker exec -it 21d spark-submit \
    --master spark://spark-master:7077 \ 
    --jars /opt/bitnami/spark/jars/spark-sql-kafka-0-10_2.13-3.4.3.jar,/opt
/bitnami/spark/jars/spark-cassandra-connector_2.12-3.4.0.jar /opt/bitnami/spark/spark_stream.py