import logging

from rabbitmq.asynchronous_consumer_example import ExampleConsumer
from rabbitmq.asynchronous_publisher_example import ExamplePublisher


LOG_FORMAT = ('%(levelname) -10s %(asctime)s %(name) -30s %(funcName) '
              '-35s %(lineno) -5d: %(message)s')

logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

example_publisher = ExamplePublisher(
    'amqp://guest:guest@localhost:5672/%2F?connection_attempts=3&heartbeat=3600'
)
example_cosumer = ExampleConsumer('amqp://guest:guest@localhost:5672/%2F?connection_attempts=3&heartbeat=3600')