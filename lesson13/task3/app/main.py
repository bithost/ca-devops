from flask import Flask
import redis
from rq import Queue
from api import getCatImage  # Assuming getCatImage function exists in api module

app = Flask(__name__)

# Configure Redis connection
r = redis.Redis(host='redis', port=6379)
q = Queue(connection=r)

@app.route('/')
def index():
    # Enqueue a job
    task = q.enqueue(getCatImage, 5)
    n = len(q.jobs)

    html = '<center><br /><br />'
    for job in q.jobs:
        html += f'<a href="job/{job.id}">{job.id}</a><br /><br />'
    html += f'Total {n} Jobs in queue </center>'
    return f"{html}"

@app.route('/job/<job_id>')
def getJob(job_id):
    # Fetch job by ID
    res = q.fetch_job(job_id)

    if not res.result:
        return f'<center><br /><br /><h3>The job is still pending</h3><br /><br />ID:{job_id}<br />Queued at: {res.enqueued_at}<br />Status: {res._status}</center>'

    return f'<center><br /><br /><img src="{res.result}" height="200px"><br /><br />ID:{job_id}<br />Queued at: {res.enqueued_at}<br />Finished at: {res.ended_at}</center>'
