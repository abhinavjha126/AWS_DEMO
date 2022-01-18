var="$(grep -o [0-9] /home/ubuntu/HELM-AND-ANSIBLE/helm_deployment/values.yaml)"
var1="$(kubectl exec slurm-master-deployment-s1-58b7545b6b-nbm6f -- cat /etc/hosts | grep slurm-worker-1)"
echo $var1
