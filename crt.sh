#!/bin/bash
if [ $# -eq 0 ]; then
  echo "Usage: $0 <domain-to-filter>"
  exit 1
fi

# The domain to search for
search_domain="$1"

# enter target domain here
query_domain="test.com"

# Use curl to send a GET request to crt.sh and use jq to filter the JSON output
curl -s "https://crt.sh/?q=${query_domain}&output=json" | jq -r --arg domain "$search_domain" '.[] | select(.name_value | contains($domain)) | .name_value'

