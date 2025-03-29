import os
import json
from threading import Event
from queue import Queue
from app import webserver
from flask import request, jsonify


@webserver.route('/api/post_endpoint', methods=['POST'])
def post_endpoint():
    """Handle POST requests to the /api/post_endpoint route."""
    if request.method == 'POST':
        data = request.json
        print(f"got data in post {data}")
        response = {"message": "Received data successfully", "data": data}
        return jsonify(response)
    return jsonify({"error": "Method not allowed"}), 405


@webserver.route('/api/graceful_shutdown', methods=['GET'])
def graceful_shutdown():
    """Initiate a graceful shutdown of the web server."""
    webserver.tasks_runner.shutdown_event.set()
    webserver.tasks_runner.job_queue.join()
    for thread in webserver.tasks_runner.threads:
        thread.join()
    return "Shutdown process has started", 200


@webserver.route('/api/get_results/<job_id>', methods=['GET'])
def get_response(job_id):
    """Retrieve the results of a job by its job_id."""
    for job in webserver.tasks_runner.job_id_status:
        if job['job_id'] == job_id:
            if job['status'] == 'done':
                results_path = os.path.join('results', job['job_id'] + '.json')
                with open(results_path, 'r') as f:
                    data = json.load(f)
                return jsonify({
                    'status': 'done',
                    'data': data
                })
            return jsonify({'status': 'running'})


@webserver.route('/api/states_mean', methods=['POST'])
def states_mean_request():
    """Queue a job to calculate the mean of states."""
    data = request.json
    job_id = f'job_id_{webserver.job_counter + 1}'
    webserver.tasks_runner.job_queue.put({
        'job_id': job_id,
        'type': 'states_mean',
        'data': data
    })
    webserver.tasks_runner.job_id_status.append({
        'job_id': job_id,
        'status': 'running'
    })
    webserver.tasks_runner.job_available.set()
    webserver.job_counter += 1
    return jsonify({"job_id": job_id})


@webserver.route('/api/state_mean', methods=['POST'])
def state_mean_request():
    """Queue a job to calculate the mean of a single state."""
    data = request.json
    job_id = f'job_id_{webserver.job_counter + 1}'
    webserver.tasks_runner.job_queue.put({
        'job_id': job_id,
        'type': 'state_mean',
        'data': data
    })
    webserver.tasks_runner.job_id_status.append({
        'job_id': job_id,
        'status': 'running'
    })
    webserver.tasks_runner.job_available.set()
    webserver.job_counter += 1
    return jsonify({"job_id": job_id})


@webserver.route('/api/best5', methods=['POST'])
def best5_request():
    """Queue a job to find the best 5 results."""
    data = request.json
    job_id = f'job_id_{webserver.job_counter + 1}'
    webserver.tasks_runner.job_queue.put({
        'job_id': job_id,
        'type': 'best5',
        'data': data
    })
    webserver.tasks_runner.job_id_status.append({
        'job_id': job_id,
        'status': 'running'
    })
    webserver.tasks_runner.job_available.set()
    webserver.job_counter += 1
    return jsonify({"job_id": job_id})


@webserver.route('/api/worst5', methods=['POST'])
def worst5_request():
    """Queue a job to find the worst 5 results."""
    data = request.json
    job_id = f'job_id_{webserver.job_counter + 1}'
    webserver.tasks_runner.job_queue.put({
        'job_id': job_id,
        'type': 'worst5',
        'data': data
    })
    webserver.tasks_runner.job_id_status.append({
        'job_id': job_id,
        'status': 'running'
    })
    webserver.tasks_runner.job_available.set()
    webserver.job_counter += 1
    return jsonify({"job_id": job_id})


@webserver.route('/api/global_mean', methods=['POST'])
def global_mean_request():
    """Queue a job to calculate the global mean."""
    data = request.json
    job_id = f'job_id_{webserver.job_counter + 1}'
    webserver.tasks_runner.job_queue.put({
        'job_id': job_id,
        'type': 'global_mean',
        'data': data
    })
    webserver.tasks_runner.job_id_status.append({
        'job_id': job_id,
        'status': 'running'
    })
    webserver.tasks_runner.job_available.set()
    webserver.job_counter += 1
    return jsonify({"job_id": job_id})


@webserver.route('/api/diff_from_mean', methods=['POST'])
def diff_from_mean_request():
    """Queue a job to calculate the difference from the mean."""
    data = request.json
    job_id = f'job_id_{webserver.job_counter + 1}'
    webserver.tasks_runner.job_queue.put({
        'job_id': job_id,
        'type': 'diff_from_mean',
        'data': data
    })
    webserver.tasks_runner.job_id_status.append({
        'job_id': job_id,
        'status': 'running'
    })
    webserver.tasks_runner.job_available.set()
    webserver.job_counter += 1
    return jsonify({"job_id": job_id})


@webserver.route('/api/state_diff_from_mean', methods=['POST'])
def state_diff_from_mean_request():
    """Queue a job to calculate the state difference from the mean."""
    data = request.json
    job_id = f'job_id_{webserver.job_counter + 1}'
    webserver.tasks_runner.job_queue.put({
        'job_id': job_id,
        'type': 'state_diff_from_mean',
        'data': data
    })
    webserver.tasks_runner.job_id_status.append({
        'job_id': job_id,
        'status': 'running'
    })
    webserver.tasks_runner.job_available.set()
    webserver.job_counter += 1
    return jsonify({"job_id": job_id})


@webserver.route('/api/mean_by_category', methods=['POST'])
def mean_by_category_request():
    """Queue a job to calculate the mean by category."""
    data = request.json
    job_id = f'job_id_{webserver.job_counter + 1}'
    webserver.tasks_runner.job_queue.put({
        'job_id': job_id,
        'type': 'mean_by_category',
        'data': data
    })
    webserver.tasks_runner.job_id_status.append({
        'job_id': job_id,
        'status': 'running'
    })
    webserver.tasks_runner.job_available.set()
    webserver.job_counter += 1
    return jsonify({"job_id": job_id})


@webserver.route('/api/state_mean_by_category', methods=['POST'])
def state_mean_by_category_request():
    """Queue a job to calculate the state mean by category."""
    data = request.json
    job_id = f'job_id_{webserver.job_counter + 1}'
    webserver.tasks_runner.job_queue.put({
        'job_id': job_id,
        'type': 'state_mean_by_category',
        'data': data
    })
    webserver.tasks_runner.job_id_status.append({
        'job_id': job_id,
        'status': 'running'
    })
    webserver.tasks_runner.job_available.set()
    webserver.job_counter += 1
    return jsonify({"job_id": job_id})


@webserver.route('/')
@webserver.route('/index')
def index():
    """Display a welcome message and list available routes."""
    routes = get_defined_routes()
    msg = "Hello, World!\nInteract with the webserver using one of the defined routes:\n"
    paragraphs = ""
    for route in routes:
        paragraphs += f"<p>{route}</p>"
    msg += paragraphs
    return msg


def get_defined_routes():
    """Retrieve a list of all defined routes and their methods."""
    routes = []
    for rule in webserver.url_map.iter_rules():
        methods = ', '.join(rule.methods)
        routes.append(f'Endpoint: "{rule}" Methods: "{methods}"')
    return routes
