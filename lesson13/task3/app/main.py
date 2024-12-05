from flask import Flask, render_template_string
import redis
from rq import Queue, get_current_job
from api import getCatImage  # Ensure getCatImage function exists in api module

app = Flask(__name__)

# Configure Redis connection
try:
    r = redis.Redis(host='redis', port=6379)
    r.ping()  # Check if Redis server is reachable
except redis.ConnectionError:
    print("Could not connect to Redis. Ensure that the Redis server is running.")
    exit(1)

q = Queue(connection=r)

@app.route('/')
def index():
    # Enqueue a job and retrieve the job ID
    task = q.enqueue(getCatImage, 5)
    n = len(q.jobs)  # Get number of jobs in the queue

    # HTML response to display jobs in the queue
    html = '<center><br /><br />'
    for job in q.jobs:
        html += f'<a href="job/{job.id}">{job.id}</a><br /><br />'
    html += f'Total {n} Jobs in queue </center>'
    return render_template_string(html)

@app.route('/job/<job_id>')
def getJob(job_id):
    # Fetch job by ID
    try:
        res = q.fetch_job(job_id)
    except Exception as e:
        return f'<center>Error fetching job: {str(e)}</center>'

    if res is None:
        return f'<center><br /><br /><h3>Job ID {job_id} does not exist.</h3></center>'

    if res.result is None:
        return f'<center><br /><br /><h3>The job is still pending</h3><br />' \
               f'ID: {job_id}<br />' \
               f'Queued at: {res.enqueued_at}<br />' \
               f'Status: {res._status}</center>'
    
    return f'<center><br /><br /><img src="{res.result}" height="200px"><br /><br />' \
           f'ID: {job_id}<br />' \
           f'Queued at: {res.enqueued_at}<br />' \
           f'Finished at: {res.ended_at}</center>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
