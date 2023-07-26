FROM python:3.10.5-slim as base

LABEL maintainer="rzmobiledev@gmail.com"
ENV PYTHONUNBUFFERED 1

FROM base as builder
RUN mkdir /install
WORKDIR /install
COPY requirements.txt .
COPY /scripting /scripting

RUN apt update \
    && pip install --upgrade pip && pip install --prefix="/install" -r requirements.txt && \
    adduser --disabled-password --no-create-home \
    rizal && chmod -R +x /scripting

USER rizal

FROM base
COPY --from=builder /install /usr/local
COPY --from=builder /scripting /usr/local/bin
COPY . /app
WORKDIR /app

EXPOSE 8000
ENV PATH="/scripting:/usr/local/bin:$PATH"
CMD [ "calling.sh" ]



