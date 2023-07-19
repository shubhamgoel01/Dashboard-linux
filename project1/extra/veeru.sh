domain=${1}
port=${2}

echo $domain
echo $port
CERT_DATE=`openssl s_client -connect $domain:$port 2>/dev/null | openssl x509 -noout -text | grep "Not After"|sed 's/Not After : //'`

#date_s=$(date -d "${CERT_DATE}" +%s)
#now_s=$(date -d now +%s)
#date_diff=$(( (date_s - now_s) / 86400 ))

echo $CERT_DATE
echo $date_s
echo $now_s
echo $date_diff




# openssl s_client -connect p104.beta-wspbx.com:5061 2>/dev/null | openssl x509 -noout -text| grep "Not After"|sed 's/Not After : //'
