#!/bin/bash
var="$(grep -o [0-9] /home/ubuntu/HELM-AND-ANSIBLE/helm_deployment/values.yaml)"
USERNAME=root
HOSTS="ip-172-31-23-193"
SCRIPT="
if [[ ! -d /lustre/s$var ]]
then
sudo mkdir /lustre/s$var
fi"
for HOSTNAME in ${HOSTS} ; do
    ssh -l ${USERNAME} ${HOSTNAME} "${SCRIPT}"
done
