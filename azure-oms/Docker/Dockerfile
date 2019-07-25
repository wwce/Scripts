FROM ubuntu:16.04
MAINTAINER pglynn@paloaltonetworks.com
LABEL vendor=Microsoft\ Corp \
com.microsoft.product="OMS Container Docker Provider" \
com.microsoft.version="1.0.0-37"
ENV tmpdir /opt
ENV WSID=<WORKSPACE ID>
ENV KEY=<PRIVATE KEY>
RUN /usr/bin/apt-get update && /usr/bin/apt-get install -y libc-bin wget openssl curl sudo python-ctypes sysv-rc net-tools rsyslog cron vim dmidecode apt-transport-https && rm -rf /var/lib/apt/lists/*
COPY setup.sh main.sh custom.sh $tmpdir/
WORKDIR ${tmpdir}
RUN chmod 775 $tmpdir/*.sh; sync; $tmpdir/setup.sh; $tmpdir/custom.sh
CMD [ "/opt/main.sh" ]
