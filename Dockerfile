FROM python
WORKDIR /usr/app/
COPY . /usr/app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 6000
CMD python Flask.py