FROM python:3.11.3

WORKDIR Where_to_go/
RUN pip install "poetry==1.3.1"

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false \
    && poetry install --without dev --no-root

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1



COPY . .
EXPOSE 8000

ENTRYPOINT ["bash","entrypoint.sh" ]
CMD ["gunicorn", "Where_to_go.wsgi", "-w", "4","-b","127.0.0.1:8000"]

