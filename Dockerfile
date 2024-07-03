from python:3.12-alpine as base
FROM base as builder
RUN pip install --user hypercorn fastapi

FROM base
COPY --from=builder /root/.local /root/.local
COPY app.py /app/app.py
COPY static /app/static
WORKDIR /app
CMD ["python3" ,"-u" ,"-m" , "hypercorn", "app:app", "--bind", "0.0.0.0:80","--bind","0.0.0.0:443", "--access-log", "-", "--error-log", "-"]