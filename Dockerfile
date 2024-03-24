FROM python:3.11-alpine

WORKDIR /api

# Install gunicorn
RUN pip install gunicorn

# Install python dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy source code
COPY . .

CMD gunicorn \
        --access-logfile - \
        -b 0.0.0.0:80 \
        -k uvicorn.workers.UvicornWorker \
        app:api