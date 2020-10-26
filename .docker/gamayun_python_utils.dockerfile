FROM ibrko/gamayun:0.2.1

RUN apk add --no-cache bash \
    && apk add --no-cache python3 \
    && apk add --no-cache gcc \
    && apk add --no-cache g++ \
    && apk add --no-cache libc-dev \
    && apk add --no-cache linux-headers \
    && apk add --no-cache python3-dev \
    && python3 -m ensurepip \
    && pip3 install --upgrade pip setuptools \
    && rm -r /usr/lib/python*/ensurepip && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache \
    && pip install gamayun-utils==0.2.1.1 \
    #&& pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple gamayun-utils==0.2.0.99 \
    && pip install requests \
    && pip install BeautifulSoup4
