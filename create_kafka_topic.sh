#!/bin/bash

docker exec -it f8c /opt/bitnami/kafka/bin/kafka-topics.sh --create --bootstrap-server localhost:29092 --replication-factor 1 --partitions 1 --topic test
