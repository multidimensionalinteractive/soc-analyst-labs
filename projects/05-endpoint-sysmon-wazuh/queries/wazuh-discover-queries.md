# Wazuh Query Notes

Use these in Wazuh dashboard search or adapt them to your index naming convention.

## Sysmon Process Creation

```text
data.win.system.providerName:"Microsoft-Windows-Sysmon" AND data.win.system.eventID:1
```

## Suspicious PowerShell

```text
data.win.system.eventID:1 AND data.win.eventdata.image:*powershell.exe AND data.win.eventdata.commandLine:(*encodedcommand* OR *downloadstring* OR *frombase64string* OR *bypass*)
```

## Network Connection From Script Interpreter

```text
data.win.system.eventID:3 AND data.win.eventdata.image:(*powershell.exe OR *cmd.exe OR *wscript.exe OR *cscript.exe)
```

## Startup Folder File Creation

```text
data.win.system.eventID:11 AND data.win.eventdata.targetFilename:*\\AppData\\Roaming\\Microsoft\\Windows\\Start\ Menu\\Programs\\Startup\\*
```

## Registry Run Key Change

```text
data.win.system.eventID:13 AND data.win.eventdata.targetObject:*\\Software\\Microsoft\\Windows\\CurrentVersion\\Run*
```
