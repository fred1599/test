FROM python:3.11-alpine3.17

RUN apk update && apk upgrade

WORKDIR /app

RUN python -m venv /app/venv
ENV PATH="/app/venv/bin:${PATH}"
ENV PYDEVD_DISABLE_FILE_VALIDATION 1

COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt
RUN pip install debugpy

RUN adduser -D fred
RUN chown -R fred /app

USER fred

COPY . /app

# Pour lancer les tests unitaires
# CMD ["pytest", "test.py"]

# Pour lancer l'application
# CMD ["python", "main.py", "data.log"]

# Pour utiliser l'outil debug de vscode
# CMD ["python", "-Xfrozen_modules=off", "-m", "debugpy", "--listen", "0.0.0.0:5678", "--wait-for-client", "main.py", "data.log"]
