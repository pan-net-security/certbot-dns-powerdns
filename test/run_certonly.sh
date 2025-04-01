#!/bin/sh

# creates a unique tmpdir, if mktemp is not found, creates /tmp/<date>
TEMP_DIR=$(mktemp -d 2>/dev/null || echo '/tmp/'$(date +%Y-%m-%d-%H-%M-%S)  )
OUTPUT_FILE="$TEMP_DIR/output"

if [ -z $1 ]; then
  echo "Usage: ./$0 /path/to/credentials.ini"
  exit 1
fi

if [ ! -f $1 ]; then
  echo "'$1' was not found, try using a absolute path instead..."
  exit 1
fi


echo "# Logs, certificates, keys, accounts will be contained in '$TEMP_DIR'"

mkdir -p $TEMP_DIR/var/log/letsencrypt \
        $TEMP_DIR/etc/letsencrypt \
        $TEMP_DIR/var/lib/letsencrypt

chmod -R 0755 $TEMP_DIR/var/log/letsencrypt \
              $TEMP_DIR/etc/letsencrypt \
              $TEMP_DIR/var/lib/letsencrypt

certbot \
        --dns-powerdns-credentials $1 \
        --dns-powerdns-propagation-seconds 20 \
        --authenticator dns-powerdns \
        --logs-dir $TEMP_DIR/var/log/letsencrypt/ \
        --server https://localhost:14000/dir \
        --work-dir $TEMP_DIR/var/lib/letsencrypt \
        --config-dir $TEMP_DIR/etc/letsencrypt \
        --domains test.example.org \
        --email admin@example.org \
        --non-interactive \
        --no-verify-ssl  \
        --agree-tos \
        --debug \
        certonly | tee -a $OUTPUT_FILE

echo "# Files created in '$TEMP_DIR': "
find ${TEMP_DIR:-/tmp}/

set -e
grep -qi 'Successfully received certificate.' $OUTPUT_FILE

