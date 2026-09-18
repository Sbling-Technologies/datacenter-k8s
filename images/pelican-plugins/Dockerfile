FROM alpine:3.24.2@sha256:294b683cb724975bec92580e1e685676bd4b50bda910ddb8c51d4cabeaec77e6 as builder

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
