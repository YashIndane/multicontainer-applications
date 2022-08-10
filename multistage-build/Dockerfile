#Model building stage

FROM docker.io/yashindane/keras-flask:v1 AS builder

COPY dataset/ /build

COPY train.py /build

WORKDIR /build

RUN pip3 install Pillow && \
    python3 train.py

#Creating final image

FROM docker.io/yashindane/keras-flask:v1

MAINTAINER Yash Indane

EXPOSE 1556

WORKDIR /pred

#Copying only the cnn model from above stage
COPY --from=builder /build/cat-dog-final.h5 .

COPY templates/ ./templates

COPY app.py .

RUN pip3 install numpy Pillow

ENTRYPOINT ["python3", "app.py"]

