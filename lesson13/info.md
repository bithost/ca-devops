https://github.com/ligurio/awesome-ci

https://agola.io/

https://woodpecker-ci.org/docs/intro

https://wilw.dev/blog/2023/04/23/woodpecker-ci/

https://oramind.com/private-cicd-using-gitlab-docker/



GRANT ALL PRIVILEGES ON gitea.* TO 'gitea'@'localhost' IDENTIFIED BY "khasdjkh&@lasdk333";



stages:
  - build
  - deploy

build:
  stage: build
  ## Run on the specified gitlab-runner with docker-in-docker
  tags:
    - aws-ubnt-runner
  image: docker:latest
  services:
    - name: docker:dind
      alias: docker
  variables:
    #DOCKER_TLS_CERTDIR: "/certs"
    DOCKER_HOST: tcp://docker:2375
    DOCKER_TLS_CERTDIR: ""
    DOCKER_DRIVER: overlay2
  before_script:
    - docker info
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
  script:
    - docker pull $CI_REGISTRY_IMAGE:latest || true
    - docker-compose -f docker-compose.yaml pull
    - docker-compose -f docker-compose.yaml build
    - docker-compose -f docker-compose.yaml push




stages:
  - build
  - deploy

build:
  stage: build
  ## Run on the specified gitlab-runner with docker-in-docker
  tags:
    - aws-ubnt-runner
  image: docker:latest
  services:
    - name: docker:dind
      alias: docker
  variables:
    #DOCKER_TLS_CERTDIR: "/certs"
    DOCKER_HOST: tcp://docker:2375
    DOCKER_TLS_CERTDIR: ""
    DOCKER_DRIVER: overlay2
  before_script:
    - docker info
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
  script:
    - echo $CI_REGISTRY_PASSWORD |docker login -u $CI_REGISTRY_USER $CI_REGISTRY --password-stdin
    - docker compose build --project-name $CI_REGISTRY_IMAGE
    - docker push $CI_REGISTRY_IMAGE
