#!/bin/bash

# List of certificate files
cert_files=(
    "cfgtre.beta-wspbx.com.crt"
    "fwdin.beta-wspbx.com.crt"
    "mp88.beta-wspbx.com.crt"
    "p101.beta-wspbx.com.crt"
    "p103.beta-wspbx.com.crt"
    "p104.beta-wspbx.com.crt"
    "p107.beta-wspbx.com.crt"
    "p201.beta-wspbx.com.crt"
    "p801.beta-wspbx.com.crt"
    "SANp103.beta-wspbx.com.crt"
    "sms-wspbx-com.crt"
    "wild.beta-wspbx.com.crt"
    "clients.crt"
)

# Declare an associative array to store days left for each certificate
declare -A days_left_array

# Iterate through each certificate file
for cert_file in "${cert_files[@]}"; do
    enddate=$(date -d "$(openssl x509 -enddate -noout -in $cert_file | cut -d= -f2)" '+%s')
    currentdate=$(date '+%s')
    ((diff=enddate-currentdate))
    ((days=diff/(60*60*24)))
    days_left_array[$cert_file]=$days
done

# Print the values stored in the associative array
for cert_file in "${!days_left_array[@]}"; do
    echo "Certificate $cert_file: Days left until expiration: ${days_left_array[$cert_file]}"
done

