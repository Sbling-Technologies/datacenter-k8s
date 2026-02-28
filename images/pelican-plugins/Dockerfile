FROM alpine:3.23.3@sha256:25109184c71bdad752c8312a8623239686a9a2071e8825f20acb8f2198c3f659 as builder

WORKDIR /builder
RUN wget --quiet https://github.com/pelican-dev/plugins/archive/refs/heads/main.zip \
    && unzip main.zip \
    && rm main.zip \
    && find plugins-main -maxdepth 1 -type f -delete \
    && find plugins-main -maxdepth 1 -type d -name ".*" -exec rm -rf {} +

ARG INCLUDE_THEMES=false
RUN if [ "$INCLUDE_THEMES" != "true" ]; then \
    find plugins-main -maxdepth 1 -type d -name "*-theme" -exec rm -rf {} +; \
    find plugins-main -maxdepth 1 -type d -name "*-language" -exec rm -rf {} +; \
    fi

FROM scratch
COPY --from=builder /builder/plugins-main /
