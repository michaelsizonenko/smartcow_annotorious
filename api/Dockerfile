FROM python:3.7
RUN mkdir /backend
WORKDIR /backend
RUN pip install gunicorn
RUN pip install Flask-SQLAlchemy
COPY requirements.txt /backend/requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
COPY . .
