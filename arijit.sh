var="$(grep -o [0-9] /home/ubuntu/HELM-AND-ANSIBLE/helm_deployment/values.yaml)"
if [[ ! -d /lustre/s$var ]]
then
sudo mkdir /lustre/s$var
fi
