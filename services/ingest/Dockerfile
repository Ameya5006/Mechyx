FROM golang:1.22-alpine

WORKDIR /app

COPY go.mod ./
RUN go mod download

COPY . .

RUN go build -o ingest-service ./

EXPOSE 8081

CMD ["./ingest-service"]
