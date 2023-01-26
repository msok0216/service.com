FROM redis:5.0.9
# WORKDIR /app
# COPY . /app
ENV REDIS_HOST=localhost
ENV REDIS_PORT=6379
CMD ["redis-server"]
EXPOSE 6379