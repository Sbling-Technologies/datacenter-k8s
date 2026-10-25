FROM alpine:3.24.3@sha256:be2656061b536c1883c4034790e21d0a09c5aaaf51968b89368a3c0371ea2c9a as builder

WORKDIR /builder
RUN wget --quiet https://github.com/pelican/plugins/archive/refs/heads/main.zip \
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
