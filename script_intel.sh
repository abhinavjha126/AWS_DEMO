#!/bin/bash
var="$(grep -o [0-9] /home/ubuntu/AWS_DEMO/helm_deployment/values.yaml)"
USERNAME=sdp
HOSTS="10.14.20.128"
PASSWORDS="redHAT733#@+"
SCRIPT="
if [[ ! -d /lustre/s$var ]]
then
mkdir /lustre/s$var
fi"
for HOSTNAME in ${HOSTS} ; do
    sshpass -p ${PASSWORDS}  ssh -l ${USERNAME} ${HOSTNAME} "${SCRIPT}"
done
helm install deployment-$var ./helm_deployment
sleep 30
a=$(kubectl get pods -o=jsonpath='{range .items..metadata}{.name}{"\n"}{end}' | fgrep slurm-master-deployment-s$var)
b=$(kubectl get pod $a --output="jsonpath={.status.containerStatuses[*].ready}" | cut -d' ' -f2)
if [ "$b" = "true" ]
then
   sum=$(( $var + 1 ))
   echo number: $sum > "/home/ubuntu/AWS_DEMO/helm_deployment/values.yaml"
fi
