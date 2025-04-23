FROM golang:1.21 AS builder

WORKDIR /app
COPY go.mod ./
COPY main.go ./
RUN go mod download
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o app

FROM alpine:latest
WORKDIR /root
COPY --from=builder /app/app .
EXPOSE 8080
CMD [ "./app" ]