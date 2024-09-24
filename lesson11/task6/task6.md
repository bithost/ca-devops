# TLS for Docker daemon on Windows

Requirments
1. Know how to use OpenSSL
2. Install OpenSSL on Windows as it doesn't come preinstalled by default

How to
1. Generate Certficiate Authority certificate
2. Once you have CA file you can create CSR (certificate signing request) to request certificate for your docker daemon
3. When you generated required certificates run Docker daemon

```shell
dockerd \
    --tlsverify \
    --tlscacert=ca.pem \
    --tlscert=server-cert.pem \
    --tlskey=server-key.pem \
    -H=0.0.0.0:2376
```

More info on how to do it:
https://docs.docker.com/engine/security/protect-access/