FROM python:3.11

WORKDIR /Elias

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app /Elias/src
ENV PYTHONPATH=/Elias/src

CMD ["uvicorn", "src.main:app","--host","0.0.0.0","--port","8000","--reload"]