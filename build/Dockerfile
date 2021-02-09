# by ahrechanychenko 29/11/20
# Use specified image and app version to keep image stable
# Add user without privilleged access to improve security
# Copy SSL certificates from build stage, because scratch images doesn't contains that
FROM alpine:3.12.1 as build
RUN apk --no-cache add gcc \
                       make \
                       musl-dev \
                       openssl-dev \
                       openssl-libs-static \
                       file \
                       git0 \
                       autoconf \
                       automake \
                       libtool \
    && adduser -D -g '' curl
USER curl
RUN git clone https://github.com/curl/curl /tmp/curl/ \
    && cd /tmp/curl \
    && git checkout $(git describe --tags `git rev-list --tags --max-count=1`) \
    && autoreconf -fi \
    && ./configure --disable-shared --enable-optimize --disable-dependency-tracking \
    && make curl_LDFLAGS=-all-static

FROM scratch as production
COPY --from=build /etc/passwd/ /etc/passwd
COPY --from=build /tmp/curl/src/curl .
COPY --from=build /etc/ssl /etc/ssl
USER curl
ENTRYPOINT ["./curl"]
