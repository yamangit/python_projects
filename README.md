# python_projects
All kinds of python scripts and API's

## Usage

### 1. Clone the repository
```bash
git clone https://github.com/yamangit/python_projects.git
```

### 2. Make Python environment
```bash
cd python_projects
python3 -m venv pyenv
source pyenv/bin/activate
pip install -r requirements.txt
cd Juniper_logprocrssing
```

#### 3. Run the script
```bash
python3 Script_Logprocessing.py
```
## Log samples

### 1. UI_CMDLINE_READ_LINE
```log
Jun 24 18:42:01 <hostname> <host ip>: mgd[40408]: UI_CMDLINE_READ_LINE: User '<username>', command 'show interfaces descriptions '
Jun 24 18:42:03 <hostname> <host ip>: mgd[40408]: UI_CMDLINE_READ_LINE: User '<username>', command 'show interfaces diagnostics optics xe-0/0/17 '
```

### 2. RPD_RSVP_NBRDOWN and RPD_RSVP_NBRUP
```log
Jun 24 01:00:46 <hostname> <host ip>: rpd[5566]: RPD_RSVP_NBRDOWN: RSVP neighbor <ip> down on interface ae0.177 nbr-type Direct, triggered by IGP neighbor down event
Jun 24 01:00:57 <hostname> <host ip>: rpd[6988]: RPD_RSVP_NBRUP: RSVP neighbor <ip> up on interface ae0.177 nbr-type Direct
```
### 3. SNMP_EVLIB_FAILURE
```log
Jun 24 12:10:14 <hostname> <host ip>: mib2d[11904]: SNMP_EVLIB_FAILURE: PFED ran out of transfer credits with PFE.Failed to get stats. ifl index: 6155 

```
### 4. 
```log
Jun 24 02:34:25 <hostname> <host ip>: jddosd[23182]: DDOS_PROTOCOL_VIOLATION_SET: Warning: Host-bound traffic for protocol/exception  DHCPv4v6:aggregate exceeded its allowed bandwidth at fpc 0 for 608 times, started at 2023-06-24 02:34:24 NPT
Jun 24 02:35:22 <hostname> <host ip>: jddosd[13160]: DDOS_PROTOCOL_VIOLATION_CLEAR: INFO: Host-bound traffic for protocol/exception PPPoE:padi has returned to normal. Its allowed bandwith was exceeded at fpc 0 for 134 times, from 2023-06-23 07:12:31 NPT to 2023-06-24 02:30:21 NPT
```
### 5. LOGIN_PAM_AUTHENTICATION_ERROR, LOGIN_INFORMATION, LOGIN_FAILED, SSHD_LOGIN_FAILED and PAM_SSHD
```log
Jun 24 04:41:58 <hostname> <host ip>: login[28685]: LOGIN_PAM_AUTHENTICATION_ERROR: Failed password for user user1
Jun 24 17:45:59 <hostname> <host ip>: login[71127]: LOGIN_INFORMATION: User user6 logged in from host 11.5.6.7 on device pts/0
Jun 24 12:46:25 <hostname> <host ip>: login[93054]: LOGIN_FAILED: Login failed for user wow from host 45.67.8.9
un 24 02:09:05 <hostname> <host ip>: sshd: SSHD_LOGIN_FAILED: Login failed for user 'tryit' from host '34.5.6.7.8'
```
so on ........

