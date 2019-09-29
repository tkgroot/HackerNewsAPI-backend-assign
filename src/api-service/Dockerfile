FROM python:3.7-slim

ENV INSTALL_PATH="/api-service"
ENV VENV="${INSTALL_PATH}/.venv/bin"
ENV POETRY="~/.poetry/bin"
ENV PATH="${POETRY}:${VENV}:$PATH"
ENV NLTK_DATA="${INSTALL_PATH}/nltk_data"

RUN mkdir -p ${INSTALL_PATH}
WORKDIR ${INSTALL_PATH}

COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock
RUN apt-get update && \
  apt-get install -y curl git && \
  apt-get clean && \
  apt-get autoremove && \
  curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python && \
  export PATH=$HOME/.poetry/bin:$PATH && \
  poetry self:update && \
  poetry config settings.virtualenvs.in-project true && \
  poetry install && \
  python -m nltk.downloader stopwords punkt averaged_perceptron_tagger wordnet

COPY . .

# ENTRYPOINT [ "executable" ]
CMD flask run
