from log_pattern import *
import itertools
import re
from sh import tail, zcat
from datetime import datetime
from database_queries import *


def time_format(log):

    if log.split()[1] == '1':
        day = '01'
    elif log.split()[1] == '2':
        day = '02'
    elif log.split()[1] == '3':
        day = '03'
    elif log.split()[1] == '4':
        day = '04'
    elif log.split()[1] == '5':
        day = '05'
    elif log.split()[1] == '6':
        day = '06'
    elif log.split()[1] == '7':
        day = '07'
    elif log.split()[1] == '8':
        day = '08'
    elif log.split()[1] == '9':
        day = '09'
    else:
        day = log.split()[1]

    if log.split()[0] == 'Jan':
        timestamp = f"{datetime.now().strftime('%Y')}-01-{day} {log.split()[2]}"
    elif log.split()[0] == 'Feb':
        timestamp = f"{datetime.now().strftime('%Y')}-02-{day} {log.split()[2]}"
    elif log.split()[0] == 'Mar':
        timestamp = f"{datetime.now().strftime('%Y')}-03-{day} {log.split()[2]}"
    elif log.split()[0] == 'Apr':
        timestamp = f"{datetime.now().strftime('%Y')}-04-{day} {log.split()[2]}"
    elif log.split()[0] == 'May':
        timestamp = f"{datetime.now().strftime('%Y')}-05-{day} {log.split()[2]}"
    elif log.split()[0] == 'Jun':
        timestamp = f"{datetime.now().strftime('%Y')}-06-{day} {log.split()[2]}"
    elif log.split()[0] == 'Jul':
        timestamp = f"{datetime.now().strftime('%Y')}-07-{day} {log.split()[2]}"
    elif log.split()[0] == 'Aug':
        timestamp = f"{datetime.now().strftime('%Y')}-08-{day} {log.split()[2]}"
    elif log.split()[0] == 'Sep':
        timestamp = f"{datetime.now().strftime('%Y')}-09-{day} {log.split()[2]}"
    elif log.split()[0] == 'Oct':
        ttimestamp = f"{datetime.now().strftime('%Y')}-10-{day} {log.split()[2]}"
    elif log.split()[0] == 'Nov':
        timestamp = f"{datetime.now().strftime('%Y')}-11-{day} {log.split()[2]}"
    elif log.split()[0] == 'Dec':
        timestamp = f"{datetime.now().strftime('%Y')}-12-{day} {log.split()[2]}"
    return timestamp


# try:
for line in tail('-f', '/var/log/messages', _iter=True):
# for line in zcat('/var/log/messages-20230507-11.gz', _iter=True):

    # 1.###################################### Capture Only show or run command###################################################
    if re.compile(UI_CMDLINE_READ_LINE_SHOW()).findall(str(line)):
        dat = list(itertools.chain(
            *re.compile(UI_CMDLINE_READ_LINE()).findall(str(line))))
        insert_data = [time_format(dat[0])]
        dat.pop(0)
        insert_data.extend(dat)
        newdata = [insert_data[0], "COMMAND", insert_data[1], insert_data[2],
                   insert_data[3], insert_data[4], None, insert_data[5]]
        column = ["timestamp", "log_type", "hostname", "host_ip",
                  "event", "user_login", "write_cli", "read_cli"]
        InsertData("command_line", newdata, column)
        print(newdata)

    # 2.###################################### Capture Only set command############################################################
    if re.compile(UI_CMDLINE_READ_LINE_SET()).findall(str(line)):
        dat = list(itertools.chain(
            *re.compile(UI_CMDLINE_READ_LINE()).findall(str(line))))
        insert_data = [time_format(dat[0])]
        dat.pop(0)
        insert_data.extend(dat)
        newdata = [insert_data[0], "COMMAND", insert_data[1], insert_data[2],
                   insert_data[3], insert_data[4], insert_data[5], None]
        column = ["timestamp", "log_type", "hostname", "host_ip",
                  "event", "user_login", "write_cli", "read_cli"]
        InsertData("command_line", newdata, column)
        print(newdata)

    # 3.###################################### Capture Mac Pinning Log##############################################################
    elif re.compile(L2ALD_MAC_PINNING_DISCARD_NOTIFICATION()).findall(str(line)):
        dat = list(itertools.chain(
            *re.compile(L2ALD_MAC_PINNING_DISCARD_NOTIFICATION()).findall(str(line))))
        insert_data = [time_format(dat[0])]
        dat.pop(0)
        insert_data.extend(dat)
        newdata = [insert_data[0], "MAC_PINNING", insert_data[1], insert_data[2], insert_data[3],
                   insert_data[4], insert_data[5], insert_data[6] , insert_data[7], insert_data[8]]
        print(newdata)
        column = ["timestamp", "log_type", "hostname", "event", "mac_address",
                  "domain_type", "bridge_domain", "interface_from", "action", "interface_on"]
        InsertData('mac_pinning', newdata, column)

    # 4.###################################### Capture RSVP UP Log##############################################################
    elif re.compile(RPD_RSVP_NBRUP()).findall(str(line)):
        dat = list(itertools.chain(
            *re.compile(RPD_RSVP_NBRUP()).findall(str(line))))
        insert_data = [time_format(dat[0])]
        dat.pop(0)
        insert_data.extend(dat)
        newdata = [insert_data[0], "RPD_NBR", insert_data[1], insert_data[2],
                   insert_data[3], insert_data[4], insert_data[5], insert_data[6], insert_data[7]]
        column = ["timestamp", "log_type", "hostname", "host_ip",
                  "event", "dest_ip", "status", "interface", "rpd_type"]
        InsertData("rpd_nbr_log", newdata, column)
        print(newdata)

    # 5.###################################### Capture RSVP Down Log##############################################################
    elif re.compile(RPD_RSVP_NBRDOWN()).findall(str(line)):
        dat = list(itertools.chain(
            *re.compile(RPD_RSVP_NBRDOWN()).findall(str(line))))
        insert_data = [time_format(dat[0])]
        dat.pop(0)
        insert_data.extend(dat)
        newdata = [insert_data[0], "RPD_NBR", insert_data[1], insert_data[2],
                   insert_data[3], insert_data[4], insert_data[5], insert_data[6], insert_data[7]]
        column = ["timestamp", "log_type", "hostname", "host_ip",
                  "event", "dest_ip", "status", "interface", "rpd_type"]
        InsertData("rpd_nbr_log", newdata, column)
        print(newdata)

    # 6.###################################### Capture SNMP_EVLIB_FAILURE Log##############################################################
    elif re.compile(SNMP_EVLIB_FAILURE()).findall(str(line)):
        dat = list(itertools.chain(
            *re.compile(SNMP_EVLIB_FAILURE()).findall(str(line))))
        insert_data = [time_format(dat[0])]
        dat.pop(0)
        insert_data.extend(dat)
        newdata = [insert_data[0], "SNMP_EVLIB", insert_data[1],
                   insert_data[2], insert_data[3], insert_data[4], insert_data[5]]
        column = ["timestamp", "log_type", "hostname", "host_ip",
                  "event", "message", "interface_index"]
        InsertData("snmp_lib", newdata, column)
        print(newdata)

    # 7.###################################### Capture Connection to RE Log##############################################################
    elif re.compile(Connection_to_RE()).findall(str(line)):
        dat = list(itertools.chain(
            *re.compile(Connection_to_RE()).findall(str(line))))
        insert_data = [time_format(dat[0])]
        dat.pop(0)
        insert_data.extend(dat)
        newdata = [insert_data[0], "RE_LOG", insert_data[1], insert_data[2],
                   insert_data[3], insert_data[4], insert_data[5], insert_data[6]]
        column = ["timestamp", "log_type", "hostname", "host_ip",
                  "slots", "interface", "event", "status"]
        InsertData("spd_re_log", newdata, column)
        print(newdata)

    # 8.###################################### Capture Connection to SPD Failed Log##############################################################
    elif re.compile(Connection_to_SPD_Failed()).findall(str(line)):
        dat = list(itertools.chain(
            *re.compile(Connection_to_SPD_Failed()).findall(str(line))))
        insert_data = [time_format(dat[0])]
        dat.pop(0)
        insert_data.extend(dat)
        newdata = [insert_data[0], "SPD_LOG", insert_data[1], insert_data[2],
                   insert_data[3], insert_data[4], insert_data[5], insert_data[6]]
        column = ["timestamp", "log_type", "hostname", "host_ip",
                  "slots", "interface", "event", "status"]
        InsertData("spd_re_log", newdata, column)
        print(newdata)

    # 9.###################################### Capture DDOS set Log##############################################################
    elif re.compile(DDOS_PROTOCOL_VIOLATION_SET()).findall(str(line)):
        dat = list(itertools.chain(
            *re.compile(DDOS_PROTOCOL_VIOLATION_SET()).findall(str(line))))
        insert_data = [time_format(dat[0])]
        dat.pop(0)
        insert_data.extend(dat)
        newdata = [insert_data[0], "DDOS_SET", insert_data[1],
                   insert_data[2], insert_data[3],  insert_data[4],  insert_data[5], insert_data[6], insert_data[7], insert_data[8]]
        column = ["timestamp", "log_type", "hostname", "host_ip",
                  "event", "protocol", "cards", "voilation_count", 'time_start', 'time_zone']
        InsertData('ddos_set', newdata, column)
        print(newdata)

    # 10.###################################### Capture DDOS Clear Log##############################################################
    elif re.compile(DDOS_PROTOCOL_VIOLATION_CLEAR()).findall(str(line)):
        dat = list(itertools.chain(
            *re.compile(DDOS_PROTOCOL_VIOLATION_CLEAR()).findall(str(line))))
        insert_data = [time_format(dat[0])]
        dat.pop(0)
        insert_data.extend(dat)
        newdata = [insert_data[0], "DDOS_CLEAR", insert_data[1],
                   insert_data[2], insert_data[3],  insert_data[4],  insert_data[5], insert_data[6], insert_data[7], insert_data[8], insert_data[9]]
        column = ["timestamp", "log_type", "hostname", "host_ip",
                  "event", "protocol", "cards", "voilation_count", 'time_start', 'time_stop', 'time_zone']
        InsertData('ddos_clear', newdata, column)
        print(newdata)

    # 10.###################################### Capture SSH Password login failed Log##############################################################
    elif re.compile(LOGIN_PAM_AUTHENTICATION_ERROR()).findall(str(line)):
        dat = list(itertools.chain(
            *re.compile(LOGIN_PAM_AUTHENTICATION_ERROR()).findall(str(line))))
        insert_data = [time_format(dat[0])]
        dat.pop(0)
        insert_data.extend(dat)
        newdata = [insert_data[0], "PAM_AUTHENTICATION",
                   insert_data[1], insert_data[2], insert_data[3], insert_data[4], None]
        column = ["timestamp", "log_type", "hostname", "host_ip",
                  "event", "user_name", 'source_ip']
        InsertData('login_failure', newdata, column)
        print(newdata)

    # 11.###################################### Capture login Successful Log##############################################################
    elif re.compile(LOGIN_INFORMATION()).findall(str(line)):
        dat = list(itertools.chain(
            *re.compile(LOGIN_INFORMATION()).findall(str(line))))
        insert_data = [time_format(dat[0])]
        dat.pop(0)
        insert_data.extend(dat)
        newdata = [insert_data[0], 'SUCCESS_LOGIN', insert_data[1], insert_data[2],
                   insert_data[3], insert_data[4], insert_data[5], insert_data[6]]
        column = ["timestamp", "log_type", "hostname", "host_ip",
                  "event", "user_login", 'login_host', 'terminal_type']
        InsertData('login_info', newdata, column)
        print(newdata)

    # 12.###################################### Capture login Failed Telnet Log##############################################################
    elif re.compile(LOGIN_FAILED()).findall(str(line)):
        dat = list(itertools.chain(
            *re.compile(LOGIN_FAILED()).findall(str(line))))
        insert_data = [time_format(dat[0])]
        dat.pop(0)
        insert_data.extend(dat)
        newdata = [insert_data[0], 'LOGIN_FAILED', insert_data[1],
                   f"TELNET_{insert_data[3]}", insert_data[2], insert_data[4], insert_data[5]]
        column = ["timestamp", "log_type", "hostname",
                  "event", "host_ip", "user_name", "source_ip"]
        InsertData("login_failure", newdata, column)
        print(newdata)

    # 13.###################################### Capture login Failed ssh Log##############################################################
    elif re.compile(SSHD_LOGIN_FAILED()).findall(str(line)):
        dat = list(itertools.chain(
            *re.compile(SSHD_LOGIN_FAILED()).findall(str(line))))
        insert_data = [time_format(dat[0])]
        dat.pop(0)
        insert_data.extend(dat)
        newdata = [insert_data[0], 'LOGIN_FAILED', insert_data[1],
                   insert_data[3], insert_data[2], insert_data[4], insert_data[5]]
        column = ["timestamp", "log_type", "hostname",
                  "event", "host_ip", "user_name", "source_ip"]
        InsertData("login_failure", newdata, column)
        print(newdata)

    # 14.###################################### Capture MPLS path down Log##############################################################
    elif re.compile(RPD_MPLS_PATH_DOWN()).findall(str(line)):
        dat = list(itertools.chain(
            *re.compile(RPD_MPLS_PATH_DOWN()).findall(str(line))))
        insert_data = [time_format(dat[0])]
        dat.pop(0)
        insert_data.extend(dat)
        newdata = [insert_data[0], "MPLS", insert_data[1],
                   insert_data[2], insert_data[3], insert_data[4], insert_data[5], insert_data[6], None]
        column = ["timestamp", "log_type", "hostname",
                  "host_ip", 'event', "path", "status", "link", 'speed']
        InsertData("mpls_log", newdata, column)
        print(newdata)

    # 15.###################################### Capture MPLS path up Log##############################################################
    elif re.compile(RPD_MPLS_PATH_UP()).findall(str(line)):
        dat = list(itertools.chain(
            *re.compile(RPD_MPLS_PATH_UP()).findall(str(line))))
        insert_data = [time_format(dat[0])]
        dat.pop(0)
        insert_data.extend(dat)
        newdata = [insert_data[0], "MPLS", insert_data[1],
                   insert_data[2], insert_data[3], insert_data[4], insert_data[5], insert_data[6], insert_data[7]]
        column = ["timestamp", "log_type", "hostname",
                  "host_ip", 'event', "path", "status", "link", 'speed']
        InsertData("mpls_log", newdata, column)
        print(newdata)

    # 16.###################################### Capture PAM SSHD Log##############################################################
    elif re.compile(PAM_SSHD()).findall(str(line)):
        dat = list(itertools.chain(
            *re.compile(PAM_SSHD()).findall(str(line))))
        insert_data = [time_format(dat[0])]
        dat.pop(0)
        insert_data.extend(dat)
        newdata = [insert_data[0], "PAM_AUTHENTICATION", insert_data[1],
                   f"LOGIN_{insert_data[3]}_AUTHENTICATION_ERROR", insert_data[2], insert_data[4], insert_data[5]]
        column = ["timestamp", "log_type", "hostname",
                  "event", "host_ip", "user_name", "source_ip"]
        InsertData("login_failure", newdata, column)
        print(newdata)
    # 17.###################################### Capture Juniper temperature Log##############################################################
    elif re.compile(jun_Temperature()).findall(str(line)):
        dat = list(itertools.chain(
                *re.compile(jun_Temperature()).findall(str(line))))
        insert_data = [time_format(dat[0])]
        dat.pop(0)
        insert_data.extend(dat)
        newdata = [insert_data[0], insert_data[3],insert_data[1], insert_data[2], insert_data[4], insert_data[5]]
        column = ["timestamp", "log_type", "hostname", "host_ip", "device_serial", "temperature"]
        InsertData("temperature_log", newdata, column)
        print(newdata)  
# except:
#     pass

# CreateTable("login_failure")
