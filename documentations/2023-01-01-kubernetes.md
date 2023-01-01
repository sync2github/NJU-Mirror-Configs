Kubernetes 是用于自动部署，扩展和管理容器化应用程序的开源系统。详情可见 [官方介绍](https://kubernetes.io/zh/)。

**硬件架构: `x86_64`, `armhfp`, `aarch64`**

### Debian/Ubuntu 用户

首先导入 gpg key：

```shell
$ sudo curl -fsSLo /usr/share/keyrings/kubernetes-archive-keyring.gpg https://packages.cloud.google.com/apt/doc/apt-key.gpg
```

新建 `/etc/apt/sources.list.d/kubernetes.list`，内容为

```
deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://mirrors.nju.edu.cn/kubernetes/apt kubernetes-xenial main
```


### RHEL/CentOS 用户

以 CentOS 7 为例， 新建 `/etc/yum.repos.d/kubernetes.repo`，内容为：

```
[kubernetes]
name=kubernetes
baseurl=https://mirror.nju.edu.cn/kubernetes/yum/repos/kubernetes-el7-$basearch
enabled=1
```

### Minikube

请到 [minikube 镜像](https://mirror.nju.edu.cn/github-release/kubernetes/minikube/LatestRelease/) 下载。
