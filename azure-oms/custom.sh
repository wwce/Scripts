#!/bin/bash
echo "===> Adding omsagent rsyslog configuration..."
echo '#OMS_facility = local4' >> /etc/rsyslog.d/security-config-omsagent.conf
echo 'local4.debug	@127.0.0.1:25226' >> /etc/rsyslog.d/security-config-omsagent.conf
echo "===> Enabling syslog reception on UDP/514"
echo '# provides UDP syslog reception' >> /etc/rsyslog.conf
echo 'module(load="imudp")' >> /etc/rsyslog.conf
echo 'input(type="imudp" port="514")' >> /etc/rsyslog.conf
systemctl enable rsyslog
systemctl start rsyslog
echo "===> Download OMS agent configuration..."
mkdir -p /etc/opt/microsoft/omsagent/${WSID}/conf/omsagent.d/
curl -o /etc/opt/microsoft/omsagent/${WSID}/conf/omsagent.d/security_events.conf https://raw.githubusercontent.com/Microsoft/OMS-Agent-for-Linux/master/installer/conf/omsagent.d/security_events.conf
