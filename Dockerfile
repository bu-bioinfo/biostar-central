FROM continuumio/miniconda3:4.11.0

RUN apt-get update && apt-get -y install build-essential

RUN mkdir /biostar-central.
COPY environment.yml /biostar-central/
COPY conf /biostar-central/conf

WORKDIR /biostar-central

RUN conda env create -f environment.yml

SHELL ["conda", "run", "-n", "engine", "/bin/bash", "-c"]

RUN pip install -r /biostar-central/conf/requirements.txt

RUN conda config --add channels r
RUN conda config --add channels conda-forge
RUN conda config --add channels bioconda
RUN conda install --file /biostar-central/conf/conda-packages.txt

COPY docs /biostar-central/docs
COPY export /biostar-central/export
COPY initial /biostar-central/inital
COPY themes /biostar-central/themes
COPY *.* /biostar-central/
COPY Makefile /biostar-central/

COPY biostar /biostar-central/biostar

RUN python manage.py migrate --settings biostar.forum.settings
RUN python manage.py collectstatic --noinput -v 0 --settings biostar.forum.settings

RUN make forum init
RUN make forum test

ENTRYPOINT ["conda", "run", "-n", "engine", "make", "forum", "uwsgi"]
