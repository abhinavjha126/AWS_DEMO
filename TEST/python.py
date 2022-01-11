from typing import List


class Labels:
    app: slurm-master-s1
    group: slurm-master-s2

    def __init__(self, app: slurm-master-s1, group: slurm-master-s1) -> None:
        self.app = app
        self.group = group


class Metadata:
    name: slurm-master-deployment-s1
    labels: Labels

    def __init__(self, name: slurm-master-deployment-s1, labels: Labels) -> None:
        self.name = name
        self.labels = labels


class Selector:
    match_labels: Labels

    def __init__(self, match_labels: Labels) -> None:
        self.match_labels = match_labels


class MatchExpression:
    key: kubernetes.io/hostname
    operator: In
    values: List[b5r13u15]

    def __init__(self, key: kubernetes.io/hostname, operator: In, values: List[b5r13u15]) -> None:
        self.key = key
        self.operator = operator
        self.values = values


class LabelSelector:
    match_expressions: List[MatchExpression]

    def __init__(self, match_expressions: List[MatchExpression]) -> None:
        self.match_expressions = match_expressions


class RequiredDuringSchedulingIgnoredDuringExecution:
    label_selector: LabelSelector
    topology_key: kubernetes.io/hostname

    def __init__(self, label_selector: LabelSelector, topology_key: kubernetes.io/hostname) -> None:
        self.label_selector = label_selector
        self.topology_key = topology_key


class PodAntiAffinity:
    required_during_scheduling_ignored_during_execution: List[RequiredDuringSchedulingIgnoredDuringExecution]

    def __init__(self, required_during_scheduling_ignored_during_execution: List[RequiredDuringSchedulingIgnoredDuringExecution]) -> None:
        self.required_during_scheduling_ignored_during_execution = required_during_scheduling_ignored_during_execution


class Affinity:
    pod_anti_affinity: PodAntiAffinity

    def __init__(self, pod_anti_affinity: PodAntiAffinity) -> None:
        self.pod_anti_affinity = pod_anti_affinity


class VolumeMount:
    mount_path: /etc/slurm
    name: slurm-lustre-vol1

    def __init__(self, mount_path: /etc/slurm, name: slurm-lustre-vol1) -> None:
        self.mount_path = mount_path
        self.name = name


class Container:
    name: master-container-s{{number}}
    image: 041012/master:v18
    image_pull_policy: IfNotPresent
    volume_mounts: List[VolumeMount]

    def __init__(self, name: master-container-s{{number}}, image: 041012/master:v18, image_pull_policy: IfNotPresent, volume_mounts: List[VolumeMount]) -> None:
        self.name = name
        self.image = image
        self.image_pull_policy = image_pull_policy
        self.volume_mounts = volume_mounts


class PersistentVolumeClaim:
    claim_name: lustre-local-storage-claim1

    def __init__(self, claim_name: lustre-local-storage-claim1) -> None:
        self.claim_name = claim_name


class Volume:
    name: slurm-lustre-vol1
    persistent_volume_claim: PersistentVolumeClaim

    def __init__(self, name: slurm-lustre-vol1, persistent_volume_claim: PersistentVolumeClaim) -> None:
        self.name = name
        self.persistent_volume_claim = persistent_volume_claim


class TemplateSpec:
    affinity: Affinity
    hostname: slurm-master-s{{number}}
    volumes: List[Volume]
    containers: List[Container]

    def __init__(self, affinity: Affinity, hostname: slurm-master-s{{number}}, volumes: List[Volume], containers: List[Container]) -> None:
        self.affinity = affinity
        self.hostname = hostname
        self.volumes = volumes
        self.containers = containers


class Template:
    metadata: Metadata
    spec: TemplateSpec

    def __init__(self, metadata: Metadata, spec: TemplateSpec) -> None:
        self.metadata = metadata
        self.spec = spec


class Welcome5Spec:
    replicas: 1
    selector: Selector
    template: Template

    def __init__(self, replicas: 1, selector: Selector, template: Template) -> None:
        self.replicas = replicas
        self.selector = selector
        self.template = template


class Welcome5:
    api_version: apps/v1
    kind: Deployment
    metadata: Metadata
    spec: Welcome5Spec

    def __init__(self, api_version: apps/v1, kind: Deployment, metadata: Metadata, spec: Welcome5Spec) -> None:
        self.api_version = api_version
        self.kind = kind
        self.metadata = metadata
        self.spec = spec

