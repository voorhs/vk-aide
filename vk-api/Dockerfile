FROM python:3.10
 
WORKDIR /code

COPY ./requirements.txt ./requirements.txt
 
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

CMD ["fastapi", "run", "src/main.py", "--port", "80", "--host", "0.0.0.0"]