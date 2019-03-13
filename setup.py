#!/usr/bin/env python

from setuptools import setup, find_packages
from distutils.core import Extension
import platform
import os

INSTALL_REQUIRES = ["futures; python_version<'3.3'",
                    "enum34; python_version<'3.5'",
                    'requests']

module = Extension('confluent_kafka.cimpl',
                   libraries=['rdkafka'],
                   sources=['confluent_kafka/src/confluent_kafka.c',
                            'confluent_kafka/src/Producer.c',
                            'confluent_kafka/src/Consumer.c'])


setup(name='confluent-kafka',
      version='0.11.0',
      description='Confluent\'s Apache Kafka client for Python',
      author='Confluent Inc',
      author_email='support@confluent.io',
      url='https://github.com/matt2000/confluent-kafka-python',
      ext_modules=[module],
      packages=find_packages(exclude=("tests",)),
      data_files=[('', ['LICENSE'])],
      extras_require={
          'avro': ['fastavro', 'requests', "avro; python_version<'3'", "avro-python3; python_version>='3'"],
      })
