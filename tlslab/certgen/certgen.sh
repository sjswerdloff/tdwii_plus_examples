#!/bin/sh
# Create the root CA of the lab and, for each host, a private key and a certificate signed by that CA.
# A private key file also holds its public key, which the certificate carries.
#
# Layout:
#   The certs volume contains one directory per party so that a host can mount only its own.
#
#   ca/       rootCA.key, rootCA.pem, rootCA.srl (serial number)   the CA's own files, mounted by no host
#   project/  project.tlslab.key, project.tlslab.pem, rootCA.pem
#   dcm4che/  dcm4che.tlslab.p12 (key and certificate), rootCA.p12 (truststore), rootCA.pem
#
# Resume:
#   A step is skipped when its output file exists so that a failed run resumes at the failed step.
#   The output file of a step is written under a temporary name and renamed when the step succeeds
#   so that a failed command cannot leave a partial output file that counts as done.
#
# Reset:
#   Remove the volume with `docker compose down --volumes`.

# Stop at the first failed command or unset variable.
set -eu

# Set the output and template directories, the certificate validity in days,
# and the PKCS#12 password (this is a lab password, do not reuse it).
CERTS=/certs
CNF=/certgen
DAYS=365
P12_PASS=secret

# Function to create the CA private key and its self-signed certificate as PEM files.
# Usage: create_ca_pem
create_ca_pem() {
    local dir="$CERTS/ca"
    if [ -f "$dir/rootCA.pem" ]; then return; fi

    # Remove the host files signed by a previous CA.
    find "$CERTS" -mindepth 1 -maxdepth 1 ! -name ca -exec rm -rf {} +

    # Create the CA private key and its self-signed certificate.
    mkdir -p "$dir"
    openssl genrsa -out "$dir/rootCA.key" 2048
    openssl req -new -x509 -key "$dir/rootCA.key" -days "$DAYS" -config "$CNF/rootCA.cnf" -out "$dir/rootCA.pem.tmp"

    # Rename the output file now that the step succeeded.
    mv "$dir/rootCA.pem.tmp" "$dir/rootCA.pem"
}

# Function to issue the private key and certificate of a host as PEM files.
# Usage: issue_host_pem DIR HOST_NAME HOST_IP
issue_host_pem() {
    local dir="$CERTS/$1"
    # Export the host name and IP address for host.cnf, which reads them from the environment.
    export HOST_NAME="$2" HOST_IP="$3"
    if [ -f "$dir/$HOST_NAME.pem" ]; then return; fi
    mkdir -p "$dir"

    # Create the host private key and its signing request.
    openssl genrsa -out "$dir/$HOST_NAME.key" 2048
    openssl req -new -key "$dir/$HOST_NAME.key" -config "$CNF/host.cnf" -out "$dir/$HOST_NAME.csr"

    # Sign the request with the CA private key.
    openssl x509 -req -in "$dir/$HOST_NAME.csr" -CA "$CERTS/ca/rootCA.pem" -CAkey "$CERTS/ca/rootCA.key" \
        -CAcreateserial -days "$DAYS" -extfile "$CNF/host.cnf" -extensions v3_req -out "$dir/$HOST_NAME.pem.tmp"
    rm "$dir/$HOST_NAME.csr"

    # Copy the CA certificate for the host to verify its peers.
    cp "$CERTS/ca/rootCA.pem" "$dir/"

    # Rename the output file now that the step succeeded.
    mv "$dir/$HOST_NAME.pem.tmp" "$dir/$HOST_NAME.pem"
}

# Function to issue the private key and certificate of a host as PKCS#12 files.
# Usage: issue_host_pkcs12 DIR HOST_NAME HOST_IP
issue_host_pkcs12() {
    local dir="$CERTS/$1" host_name="$2"
    if [ -f "$dir/$host_name.p12" ]; then return; fi

    # Issue PEM files.
    issue_host_pem "$@"

    # Convert the CA certificate to a truststore, and the private key and certificate to a keystore.
    openssl pkcs12 -export -nokeys -jdktrust anyExtendedKeyUsage -in "$CERTS/ca/rootCA.pem" \
        -out "$dir/rootCA.p12" -passout "pass:$P12_PASS"
    openssl pkcs12 -export -in "$dir/$host_name.pem" -inkey "$dir/$host_name.key" -out "$dir/$host_name.p12.tmp" \
        -passout "pass:$P12_PASS"

    # Remove the PEM files that the keystore replaces.
    rm "$dir/$host_name.key" "$dir/$host_name.pem"

    # Rename the output file now that the step succeeded.
    mv "$dir/$host_name.p12.tmp" "$dir/$host_name.p12"
}

# Function to create the lab CA, then issue each host's files in the format its applications read:
# PEM for this project, PKCS#12 for the dcm4che tools.
# Usage: main
main() {
    create_ca_pem
    issue_host_pem project project.tlslab 172.30.0.10
    issue_host_pkcs12 dcm4che dcm4che.tlslab 172.30.0.20

    echo "certgen: lab certificates ready"
}

# Run the script.
main
