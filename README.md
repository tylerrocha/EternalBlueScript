# EternalBlueScript

This is a tool for automating the EternalBlue exploit. For a given range of IP addresses, the script scans for vulnerable hosts, performs the exploit and begins post-exploitation actions.

### Requirements

This project depends on Metasploit, which can be found here: https://www.metasploit.com/

### Usage

Run with the following command:

```python ./script.py IPs_to_scan```

```IPs_to_scan``` is set directly to the RHOSTS variable in metasploit, so address ranges should be formatted in the way that metasploit expects.

### Description

This tool scans for vulnerable hosts by using metasploit's smb_ms17_010 scanner and then attacks using metasploit's ms17_010_eternalblue exploit. Upon success a meterpreter shell opens and automatically executes common post-exploitation commands to exfiltrate password hashes and other network and system information. These  post-exploit commands can be altered by editing ```commands.rc```. The full scan results are saved to ```scanner.log``` and all exploit output is saved to ```spool.log```.
