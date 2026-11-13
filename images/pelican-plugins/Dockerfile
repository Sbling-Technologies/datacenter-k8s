FROM alpine:3.24.4@sha256:f59abe656b692d901e184be3445e084786602108599d2a51d229c0f5a48c71bf as builder

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
