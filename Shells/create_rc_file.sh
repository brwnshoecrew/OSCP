#!/bin/bash
if [ $# -eq 0 ]; then
    echo "Usage: create_rc_file.sh [metasploit payload] [port]"
    exit 1
fi
IP=$( IP_No_Clip );
New_IP=$( echo -n $IP );

echo "
use exploit/multi/handler
set payload $1
set LHOST $New_IP
set LPORT $2
exploit -j -z
" > reverse_$2.rc

echo "
Created file in CWD at reverse_$2.rc
"
echo "
Execute rc file with msfconsole -qr reverse_$2.rc (also copied to your tmux clipboard)
"

echo "msfconsole -qr reverse_$2.rc" | clip
