# Testing TLS across hosts

The TLS lab is a [Docker Compose](https://docs.docker.com/compose/) setup, in the `tlslab` folder, that runs the CLI
applications and the [dcm4che tools](https://web.dcm4che.org/dcm4che-utilities) on two hosts of a private network.
Each host has a certificate issued for its own host name and IP address, so that a connection is made and verified as
between two real hosts, and not through `localhost`.

Docker is the only prerequisite.

## Hosts

| Host | Address | Content |
|---|---|---|
| `project.tlslab` | `172.30.0.10` | Python and the `tdwii_plus_examples` package, installed from the repository source |
| `dcm4che.tlslab` | `172.30.0.20` | The dcm4che tools (`dcm4che/dcm4che-tools` image) |

### Network

Both hosts are on the network `tlslab`, where Docker resolves their names. This network takes the addresses
`172.30.0.0` to `172.30.0.255`. Before the first start, check that this range is free:

```shell
docker run --rm --network host alpine ip route
```

No line of the output must start with `172.30.`. If one does, the range is already in use, by another Docker network
or a VPN: change it in `tlslab/compose.yaml` and `tlslab/certgen/certgen.sh`, then recreate the certificates with
`docker compose down --volumes`.

### Certificates

Before the hosts start, the `certgen` container creates a root CA for the lab and issues the private key and the
certificate of each host, signed by that CA.
They are kept in the `certs` volume, and each host mounts its own files, read-only, in `/certs`:

| Host | Files in `/certs` |
|---|---|
| `project.tlslab` | `project.tlslab.key` and `project.tlslab.pem` (PEM private key and certificate), `rootCA.pem` (CA certificate) |
| `dcm4che.tlslab` | `dcm4che.tlslab.p12` (PKCS#12 keystore), `rootCA.p12` (PKCS#12 truststore), `rootCA.pem` (CA certificate) |

The password of the PKCS#12 files is `secret`. The certificates are valid for 365 days.

## Starting and stopping the lab

From the `tlslab` folder, build the project image and start the lab:

```shell
docker compose up -d --build
```

Stop it with:

```shell
docker compose down
```

The certificates are kept between runs. To create a new CA and new certificates at the next start, remove the volume
too:

```shell
docker compose down --volumes
```

After changing the source of the package, run `docker compose up -d --build` again to install it in the project image.

## Test cases

Run the commands from the `tlslab` folder: the server in a first terminal, the client in a second one. Stop the server
with Ctrl+C before starting another one. The dcm4che options are explained in
[Testing the SCP applications with dcm4che](tls.md#with-dcm4che).

## Testing the SCP applications

### 1. echoscp accepts a TLS connection

```shell
docker compose exec project python -m tdwii_plus_examples.cli.echoscp -a ECHOSCP -p 2762 --verbose \
  --tls --tls-cert /certs/project.tlslab.pem --tls-key /certs/project.tlslab.key
```

```shell
docker compose exec dcm4che storescu -c ECHOSCP@project.tlslab:2762 \
  --tls-cipher TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 \
  --trust-store /certs/rootCA.p12 --trust-store-pass secret \
  --tls-eia-https
```

Expected: `storescu` logs the C-ECHO response with `status=0H`, and `echoscp` logs
`TLS session with 172.30.0.20:...: TLSv1.2, ECDHE-RSA-AES128-GCM-SHA256`.

### 2. dcm4che storescu refuses a server certificate without the called host name

With `echoscp` from case 1, connect to `project`, a name of the project host that is not in its certificate:

```shell
docker compose exec dcm4che storescu -c ECHOSCP@project:2762 \
  --tls-cipher TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 \
  --trust-store /certs/rootCA.p12 --trust-store-pass secret \
  --tls-eia-https
```

Expected: `storescu` fails with `No subject alternative DNS name matching project found` (`--tls-eia-https` verifies
the host name).

### 3. echoscp accepts a mutual TLS connection from a client with a trusted certificate

```shell
docker compose exec project python -m tdwii_plus_examples.cli.echoscp -a ECHOSCP -p 2762 --verbose \
  --mtls --tls-cert /certs/project.tlslab.pem --tls-key /certs/project.tlslab.key --tls-ca /certs/rootCA.pem
```

```shell
docker compose exec dcm4che storescu -c ECHOSCP@project.tlslab:2762 \
  --tls-cipher TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 \
  --trust-store /certs/rootCA.p12 --trust-store-pass secret \
  --key-store /certs/dcm4che.tlslab.p12 --key-store-pass secret \
  --tls-eia-https
```

Expected: `storescu` logs the C-ECHO response with `status=0H`, and `echoscp` logs the TLS session with
`client certificate subject: ..., commonName=dcm4che.tlslab`.

### 4. echoscp refuses a mutual TLS connection from a client without a certificate

With `echoscp` from case 3, run `storescu` with `--key-store` set to the truststore `rootCA.p12` instead of the keystore
`dcm4che.tlslab.p12`. A key store normally holds the private key and the certificate that the client presents.
`rootCA.p12` holds only the CA certificate, without a private key, so `storescu` has no certificate to present:

```shell
docker compose exec dcm4che storescu -c ECHOSCP@project.tlslab:2762 \
  --tls-cipher TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 \
  --trust-store /certs/rootCA.p12 --trust-store-pass secret \
  --key-store /certs/rootCA.p12 --key-store-pass secret \
  --tls-eia-https
```

Expected: `storescu` fails with `Broken pipe`. `echoscp` logs nothing: pynetdicom does not log the failed TLS
handshakes.

## Testing the SCU applications

### 5. storescu connects with TLS

`--tls-noauth` stops `storescp` from asking the client for a certificate:

```shell
docker compose exec dcm4che storescp -b STORESCP:11112 \
  --tls-cipher TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 \
  --key-store /certs/dcm4che.tlslab.p12 --key-store-pass secret \
  --trust-store /certs/rootCA.p12 --trust-store-pass secret \
  --tls-noauth
```

```shell
docker compose exec project python -m tdwii_plus_examples.cli.storescu --echo -aec STORESCP \
  --tls --tls-ca /certs/rootCA.pem dcm4che.tlslab 11112
```

Expected: `storescu` prints `Verification (C-ECHO) successful`, and `storescp` logs the closing of an `SSLSocket` with
`TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`.

### 6. storescu refuses a server certificate without the called host name

With `storescp` from case 5, connect to `dcm4che`, a name of the dcm4che host that is not in its certificate:

```shell
docker compose exec project python -m tdwii_plus_examples.cli.storescu --echo -aec STORESCP \
  --tls --tls-ca /certs/rootCA.pem dcm4che 11112
```

Expected: `storescu` prints `Verification (C-ECHO) failed: Association could not be established`, and logs
`Hostname mismatch, certificate is not valid for 'dcm4che'`
(see [Authentication of the remote AE](tls.md#authentication-of-the-remote-ae)).

### 7. storescu connects with mutual TLS

```shell
docker compose exec dcm4che storescp -b STORESCP:11112 \
  --tls-cipher TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 \
  --key-store /certs/dcm4che.tlslab.p12 --key-store-pass secret \
  --trust-store /certs/rootCA.p12 --trust-store-pass secret
```

```shell
docker compose exec project python -m tdwii_plus_examples.cli.storescu --echo -aec STORESCP \
  --mtls --tls-ca /certs/rootCA.pem \
  --tls-cert /certs/project.tlslab.pem --tls-key /certs/project.tlslab.key dcm4che.tlslab 11112
```

Expected: `storescu` prints `Verification (C-ECHO) successful`.

### 8. A mutual TLS server refuses storescu without --mtls

With `storescp` from case 7, run `storescu` with `--tls`:

```shell
docker compose exec project python -m tdwii_plus_examples.cli.storescu --echo -aec STORESCP \
  --tls --tls-ca /certs/rootCA.pem dcm4che.tlslab 11112
```

Expected: `storescu` prints `Verification (C-ECHO) failed: Association could not be established`, and `storescp` logs
`Empty client certificate chain`.
