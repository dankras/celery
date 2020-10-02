echo "render start command ... starting dummy flask server in the background (for health check)"

FLASK_APP=tasks.py flask run --host=0.0.0.0 &

echo "render start command ... starting celery beat"

celery beat -A tasks -l info

echo "render start command ... finished"
