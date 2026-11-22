# Securing connections with TLS

The `echoscp`, `storescp` and `upseventreceiver` CLI applications (SCPs) and the `storescu`, `upsfind`, `upscreatescu`,
`upschangestatescu`, `upswatchscu` and `upsmodifyscu` CLI applications (SCUs) can secure their connections with TLS or
mutual TLS.
TLS is off unless `--tls` or `--mtls` is given.

## Quick start

From the top level directory of the project, set up the Python environment with Poetry:

```shell
poetry install
```

Then start an application with TLS:

```shell
python tdwii_plus_examples/cli/echoscp.py --port 2762 \
  --tls --tls-cert scp.pem --tls-key scp.key
```

Or with mutual TLS:

```shell
python tdwii_plus_examples/cli/storescp.py --port 2762 \
  --mtls --tls-cert scp.pem --tls-key scp.key --tls-ca rootCA.pem
```

See [Certificates](#certificates) to create these files for testing.

With `--verbose`, the application logs the TLS session of each connection, including the subject
of the client certificate when there is one.

## CLI applications TLS Options

One of `--tls` or `--mtls` is needed to enable TLS:

| Option | Meaning |
|---|---|
| `--tls` | Use TLS |
| `--mtls` | Use mutual TLS: the remote AEs must also authenticate themselves |
| `--tls-cert FILE` | PEM certificate of the application |
| `--tls-key FILE` | PEM private key of the application |
| `--tls-ca FILE` | PEM certificate authorities trusted to verify the remote AEs |

The files needed depend on the role of the application:

| | SCP | SCU |
|---|---|---|
| `--tls` | `--tls-cert` and `--tls-key` | `--tls-ca` |
| `--mtls` | `--tls-cert`, `--tls-key` and `--tls-ca` | `--tls-ca`, `--tls-cert` and `--tls-key` |

An SCU never uses the certificate authorities of the system (Windows Certificate Manager,
macOS Keychain Access, Linux `/etc/ssl/certs`), it only trusts the ones given with `--tls-ca`.

`--tls` and `--mtls` cannot be combined, and the application refuses to start when the options are inconsistent
(for example a `--tls-*` option without `--tls` or `--mtls`, a missing file, `--tls-ca` without `--mtls` for an SCP,
or `--tls-cert` and `--tls-key` without `--mtls` for an SCU),
so that a mistake never silently leaves the connections unsecured.

## Certificates

TLS needs a **public key infrastructure (PKI)** to create, manage and use digital certificates.
The certificates and keys are not part of this repository: create your own, and keep the private keys private.
A root certificate authority (CA) is not provided either. A CA is an entity that signs certificates: an application
that trusts a CA trusts the certificates it signed. A root CA is at the top of that chain of trust, and its own
certificate is self-signed. It can delegate the signing to intermediate CAs, whose certificates it signed.

The `--tls-ca` file holds the root CAs that an application trusts to verify the remote AEs, concatenated if there are
several (it can also hold individual certificates to trust).
When the certificate of an application was signed by an intermediate CA, the `--tls-cert` file must hold that
certificate followed by the certificates of the intermediate CAs, so that the remote AEs can verify the whole chain
up to a root CA they trust.

The following creates, with [OpenSSL](https://www.openssl.org/), a root certificate authority, a certificate for a
SCP (valid for `localhost` and `127.0.0.1`) and a certificate for an SCU, for testing.
The authority key used here is not encrypted: do not use this setup in production,
where the certificates are normally issued by the PKI of the institution.

Save the configuration of the root certificate authority as `rootCA.cnf`:

```ini
[ req ]
distinguished_name = req_distinguished_name
x509_extensions    = v3_ca
prompt             = no

[ req_distinguished_name ]
O  = Springfield General Hospital
OU = IT Department
CN = Springfield General Hospital Root CA

[ v3_ca ]
subjectKeyIdentifier   = hash
authorityKeyIdentifier = keyid:always,issuer
basicConstraints       = critical, CA:true
keyUsage               = critical, digitalSignature, cRLSign, keyCertSign
```

The configuration of an application is the same for the SCP and the SCU, with its own name.
Save this one as `scp.cnf` and, for the SCU, as `scu.cnf` with `CN = RO SCU`.
The subject alternative names (`subjectAltName`) can be used to hold the host names and IP addresses a certificate
is valid for, and the common name (`CN`) can be used to identify the certificate, for instance in security log
messages.
The SCP and SCU classes of this project do not verify the host name of the remote AE against its `subjectAltName`.

```ini
[ req ]
distinguished_name = req_distinguished_name
prompt             = no

[ req_distinguished_name ]
O  = Springfield General Hospital
OU = Radiation Oncology
CN = RO SCP

[ v3_req ]
subjectKeyIdentifier   = hash
authorityKeyIdentifier = keyid,issuer
basicConstraints       = CA:FALSE
keyUsage               = critical, digitalSignature, keyEncipherment
extendedKeyUsage       = serverAuth, clientAuth
subjectAltName         = @alt_names

[ alt_names ]
DNS.1 = localhost
IP.1  = 127.0.0.1
```

Then create the root certificate authority, and the certificates signed by it:

```shell
# Root certificate authority
openssl genrsa -out rootCA.key 2048
openssl req -new -x509 -key rootCA.key -days 365 -config rootCA.cnf -out rootCA.pem

# SCP and SCU certificates
for name in scp scu; do
  openssl genrsa -out $name.key 2048
  openssl req -new -key $name.key -config $name.cnf -out $name.csr
  openssl x509 -req -in $name.csr -CA rootCA.pem -CAkey rootCA.key -CAcreateserial -days 365 \
    -extfile $name.cnf -extensions v3_req -out $name.pem
done
```

This produces `rootCA.pem` (to be trusted by the remote AEs), `scp.pem` and `scp.key` for the SCP,
and `scu.pem` and `scu.key` for the SCU.

## Checking with OpenSSL

`openssl s_client` checks that an application started as in the [Quick start](#quick-start) accepts TLS connections
and that its certificate is trusted.
Add `-cert scu.pem -key scu.key` when the application was started with `--mtls`.
With TLS 1.3, `s_client` considers the handshake complete before the server checks the client certificate, so a refusal
only shows afterwards, as the alert `certificate required`.

```shell
openssl s_client -connect localhost:2762 -servername localhost -CAfile rootCA.pem -verify_return_error
```

## Testing with DICOM tools

The [pynetdicom command line tools](https://pydicom.github.io/pynetdicom/dev/apps/index.html) do not support TLS.
[DCMTK](https://support.dcmtk.org/docs/mod_dcmnet.html) and [dcm4che](https://web.dcm4che.org/dcm4che-utilities)
do, and can be used to send DICOM messages to the applications with the certificates created above.
The examples use an application started on port 2762, with the AE title `ECHOSCP`:

```shell
python tdwii_plus_examples/cli/echoscp.py -a ECHOSCP --port 2762 \
  --mtls --tls-cert scp.pem --tls-key scp.key --tls-ca rootCA.pem --verbose
```

### DCMTK

Download and install the [DCMTK tools](https://dcmtk.org/en/dcmtk/dcmtk-tools/).
With Windows, download also the OpenSSL based security extensions, which provide the `-tls` variant of the tools
(`echoscu-tls`) used below. On Linux and macOS, use `echoscu` (DCMTK built with OpenSSL).

Verification with a client certificate, with Windows:

```shell
echoscu-tls -v +tls scu.key scu.pem +cf rootCA.pem -aec ECHOSCP localhost 2762
```

With `--mtls`, a client without certificate (anonymous TLS) is refused:

```shell
echoscu-tls -v +tla +cf rootCA.pem -aec ECHOSCP localhost 2762
```

### dcm4che

Download and install the [dcm4che utilities](https://github.com/dcm4che/dcm4che/releases).
With Windows, use the `.bat` launchers (`storescu.bat`).

dcm4che is a Java application that does not read the PEM files created above.
The next two steps create PKCS#12 files from the PEM files.

#### 1. Create the keystore

A **keystore** holds keys, each with its certificate, here the key and the certificate of the SCU.
Create it from `scu.pem` and `scu.key` with `openssl`:

```shell
openssl pkcs12 -export -in scu.pem -inkey scu.key -out scu.p12 -passout pass:secret
```

#### 2. Create the truststore

A **truststore** holds the certificates of the trusted authorities, here the root CA.
The tool to create it from `rootCA.pem` depends on the version of OpenSSL:

```shell
openssl version
```

With OpenSSL 3.2 or later, use `openssl`:

```shell
openssl pkcs12 -export -nokeys -jdktrust anyExtendedKeyUsage -in rootCA.pem -out rootCA.p12 -passout pass:secret
```

With an older version, use `keytool`, a tool of the Java JDK.
It will ask you to confirm that the certificate is trusted: answer `yes`.

```shell
keytool -importcert -keystore rootCA.p12 -storetype PKCS12 -storepass secret -file rootCA.pem -alias rootca
```

If you run `keytool` again, for instance with a new root CA, delete `rootCA.p12` first, or `keytool` will fail
because that file already has a `rootca` entry.

#### 3. Verify the connection

With no file to send, `storescu` does a verification (C-ECHO). Run it against the application started above with
`--mtls`:

```shell
storescu -c ECHOSCP@localhost:2762 \
  --tls-cipher TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 \
  --key-store scu.p12 --key-store-pass secret \
  --trust-store rootCA.p12 --trust-store-pass secret
```

About the dcm4che options:

- Giving the keystore and the truststore is not enough to secure the connection: TLS is enabled by one of the options
  `--tls`, `--tls-null`, `--tls-aes`, `--tls-3des` or `--tls-cipher`, which differ by the cipher suites they enable.
  Without one of them, the connection is not secured and the application closes it.
- Use `--tls-cipher`: according to the dcm4che help, the other options enable only suites that these applications
  refuse (no encryption, RSA key exchange, 3DES).
- dcm4che enables only TLS 1.2 by default, and options such as `--tls13` do not enable TLS by themselves.
  To use TLS 1.3, add `--tls13` and a TLS 1.3 suite: `--tls13 --tls-cipher TLS_AES_256_GCM_SHA384`.

Without `--key-store`, dcm4che uses its own default key store (`resource:key.p12`), and an application started with
`--mtls` refuses the connection.
To get the details of the TLS handshake in case of errors, run `export JAVA_OPTS="-Djavax.net.debug=all"` first.

### Testing with the SCU applications

The SCU applications of this project, such as `storescu`, can also be used. With `--echo`, `storescu` does a
verification (C-ECHO) and sends no file. Run it against the application started above with `--mtls`:

```shell
python tdwii_plus_examples/cli/storescu.py --echo -aec ECHOSCP --mtls --tls-ca rootCA.pem \
  --tls-cert scu.pem --tls-key scu.key localhost 2762
```

An SCU application always needs `--tls-ca`, to verify the certificate of the SCP.

## Testing across hosts

The [TLS lab](tls-lab.md) runs the CLI applications and the dcm4che tools on two Docker hosts, each with a certificate
issued for its own host name and IP address.
