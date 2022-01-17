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
helm install deployment-$var ./helm_deployment
sleep 30
a=$(kubectl get pods -o=jsonpath='{range .items..metadata}{.name}{"\n"}{end}' | fgrep slurm-master-deployment-s$var)
b=$(kubectl get pod $a --output="jsonpath={.status.containerStatuses[*].ready}" | cut -d' ' -f2)
if [ "$b" = "true" ]
then
   sum=$(( $var + 1 ))
   echo number: $sum > "/home/ubuntu/HELM-AND-ANSIBLE/helm_deployment/values.yaml"
fi
