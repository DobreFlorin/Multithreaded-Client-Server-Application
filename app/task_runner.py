import os
import json
from queue import Queue
from threading import Thread, Event
from global_mean import global_mean
from state_mean import state_mean
from states_mean import states_mean
from best5 import best5
from worst5 import worst5
from diff_from_mean import diff_from_mean
from state_diff_from_mean import state_diff_from_mean
from mean_by_category import mean_by_category
from state_mean_by_category import state_mean_by_category



class ThreadPool:
    """Manages a pool of threads for executing tasks concurrently.

    Attributes:
        threads (list): List of active threads.
        job_available (Event): Event to signal job availability.
        job_queue (Queue): Queue to hold pending jobs.
        shutdown_event (Event): Event to signal shutdown.
        job_id_status (list): List to track job statuses.
    """
    threads = []
    job_available = Event()
    job_queue = Queue()
    shutdown_event = Event()
    job_id_status = []

    def __init__(self):
        # You must implement a ThreadPool of TaskRunners
        # Your ThreadPool should check if an environment variable TP_NUM_OF_THREADS is defined
        # If the env var is defined, that is the number of threads to be used by the thread pool
        # Otherwise, you are to use what the hardware concurrency allows
        # You are free to write your implementation as you see fit, but
        # You must NOT:
        #   * create more threads than the hardware concurrency allows
        #   * recreate threads for each task 

        NUM_THREADS = os.getenv('TP_NUM_OF_THREADS')
        if NUM_THREADS is None:
            NUM_THREADS = os.cpu_count()

        for _ in range(NUM_THREADS):
            task_runner = TaskRunner(self.job_queue, self.job_available, self.shutdown_event, self.job_id_status)
            thread = Thread(target=task_runner.run)
            self.threads.append(thread)


class TaskRunner(Thread):
    """Executes tasks from the job queue in a separate thread.

    Attributes:
        job_available (Event): Event to signal job availability.
        job_queue (Queue): Queue to hold pending jobs.
        job_id_status (list): List to track job statuses.
    """
    job_available = Event()
    job_queue = Queue()
    job_id_status = []
 
    def __init__(self, job_queue, job_available, shutdown_event, job_id_status):
        #init necessary data structures
        self.job_queue = job_queue
        self.job_available = job_available
        self.shutdown_event = shutdown_event
        self.job_id_status = job_id_status

    def run(self):
        while True:
            # Get pending job
            # Execute the job and save the result to disk
            # Repeat until graceful_shutdown
            self.job_available.wait()       
            try:
                # Getting the job
                job = self.job_queue.get()
                
                # Computing the result
                function_name = job['type']
                function_to_be_called = globals()[function_name]
   
                if function_name == 'state_mean':
                    result = function_to_be_called(job['data']['question'], job['data']['state'])
                elif function_name == 'state_diff_from_mean':
                    result = function_to_be_called(job['data']['question'], job['data']['state'])
                elif function_name == 'state_mean_by_category':
                    result = function_to_be_called(job['data']['question'], job['data']['state'])
                else:   
                    result = function_to_be_called(job['data']['question'])

                # Writing the file
                results_path = os.path.join('results', job['job_id'] + '.json')
                with open(results_path, 'w') as file:
                    json.dump(result, file, indent=4)

                # Changing the status
                for j in self.job_id_status:
                    if j['job_id'] == job['job_id']:
                        j['status'] = 'done'

            finally:
                self.job_queue.task_done()
            self.job_available.clear()




