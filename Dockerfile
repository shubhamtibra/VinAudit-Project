# syntax=docker.io/docker/dockerfile:1.7-labs
FROM node:18-alpine AS react-build-step

COPY --exclude=**/node_modules --exclude=**/build app/react/ app/react/
RUN cd app/react && npm install \
    && npm run build \
    && rm -fr node_modules


FROM python:3.10

COPY --from=react-build-step /app/react/build app/react/build
COPY --exclude=**/react . .
RUN pip3 install pipenv && pipenv install
EXPOSE 8080
CMD ["pipenv", "run", "gunicorn", "--config", "gunicorn_config.py", "app.main:application"]