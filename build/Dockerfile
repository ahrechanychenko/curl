# by ahrechanychenko 29/11/20
# Use specified image and app version to keep image stable
# Add user without privilleged access to improve security
# Copy SSL certificates from build stage, because scratch images doesn't contains that
FROM alpine:3.12.1 as build
RUN apk --no-cache add gcc=9.3.0-r2 \
                       make=4.3-r0s \
                       musl-dev=1.1.24-r10 \
                       openssl-dev=1.1.1g-r0 \
                       openssl-libs-static=1.1.1g-r0 \
                       file=5.38-r0 \
                       git=2.26.2-r0 \
                       autoconf=2.69-r2 \
                       automake=1.16.2-r0 \
                       libtool=2.4.6-r7 \
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
