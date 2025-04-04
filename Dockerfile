FROM python:3.12-alpine

ARG UID=1000
ARG GID=1000

RUN addgroup -g ${GID} prod && \
    adduser -u ${UID} -G prod -s /bin/sh -D prod

WORKDIR /autoservice_union_backend

RUN chown -R ${GID}:${UID} /autoservice_union_backend && chmod 755 /autoservice_union_backend

COPY ./autoservice_union_backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY --chown={GID}:{UID} ./autoservice_union_backend .