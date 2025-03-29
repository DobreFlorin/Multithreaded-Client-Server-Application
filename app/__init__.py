import os
from queue import Queue
from  threading import Event
from flask import Flask
from app.data_ingestor import DataIngestor
from app.task_runner import ThreadPool



webserver = Flask(__name__)
webserver.tasks_runner = ThreadPool()

for thread in webserver.tasks_runner.threads:
    thread.start()


webserver.data_ingestor = DataIngestor("./nutrition_activity_obesity_usa_subset.csv")

webserver.job_counter = 0

from app import routes

webserver.results_folder = 'results'
if not os.path.exists(webserver.results_folder):
    os.makedirs(webserver.results_folder)
