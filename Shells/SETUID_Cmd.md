#include <stdio.h>
#include <unistd.h>

int main(int argc, const char * argv[]){
  if (argc > 1) printf("%s",execvp(argv[1], &argc[1]));
  return 0;
}

