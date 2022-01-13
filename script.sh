#!/bin/bash
var="$(grep -o [0-9] /home/ubuntu/K8S-FINAL-INTEL/CLUSTER/helm_deployment/values.yaml)"
ansible-playbook ansible.yml --extra-vars 'ansible_become_pass=redHAT733#@+' && helm install deployment-$var ./helm_deployment
sleep 20
a=$(kubectl get pods -o=jsonpath='{range .items..metadata}{.name}{"\n"}{end}' | fgrep slurm-master-deployment-s$var)
b=$(kubectl get pod $a --output="jsonpath={.status.containerStatuses[*].ready}" | cut -d' ' -f2)
if [ "$b" = "true" ]
then
   sum=$(( $var + 1 ))
   echo number: $sum > "/home/ubuntu/K8S-FINAL-INTEL/CLUSTER/helm_deployment/values.yaml"
fi
