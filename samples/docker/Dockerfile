FROM python
LABEL Author="John Doe"
COPY ./my_dir /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]