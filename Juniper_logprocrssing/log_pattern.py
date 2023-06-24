########################################### Juniper device log's All possible Patterns ##################################################

def L2ALD_MAC_PINNING_DISCARD_NOTIFICATION() -> str:
    data = "([a-zA-Z]+[^\S]+[0-9]+[^\S]+[0-9]+:[0-9]+:[0-9]+)[^\S]+([^\s]+)[^\]]+\]\:[^\S]+(L2ALD_MAC_PINNING_DISCARD_NOTIFICATION)\:[^\:]+\:[^\S]+([a-fA-F0-9:]+)\,[^\S]+[\w]+[^\S]+[\w]+[^\S]+([^\s]+)[^\S]+\_\_([^\_]+)\_\_[^\S]+[^\s]+[^\S]+[^\s]+[^\S]+[^\s]+[^\S]+[^\s]+[^\S]+([^\s]+)[^\S]+[^\s]+[^\S]+([^\s]+)[^\S]+[^\s]+[^\S]+[^\s]+[^\S]+([^\s]+)"
    return data


def UI_CMDLINE_READ_LINE() -> str:
    data = "([a-zA-Z]+[^\S]+[0-9]+[^\S]+[0-9]+:[0-9]+:[0-9]+)[^\S]+([^\s]+)[^\S]+([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})[^\]]+\]\:[^\S]+(UI_CMDLINE_READ_LINE)\:[^\S]+[^\s]+[^\S]+\'([^\']+)\'\,[^\S]+[^\s]+[^\S]+\'([^\']+)\'"
    return data


def UI_CMDLINE_READ_LINE_SET() -> str:
    data = "([a-zA-Z]+[^\S]+[0-9]+[^\S]+[0-9]+:[0-9]+:[0-9]+)[^\S]+([^\s]+)[^\]]+\]\:[^\S]+(UI_CMDLINE_READ_LINE)\:[^\S]+[^\s]+[^\S]+\'([^\']+)\'\,[^\S]+[^\s]+[^\S]+\'(set[^\']+|delete[^\']+)"
    return data


def UI_CMDLINE_READ_LINE_SHOW() -> str:
    data = "([a-zA-Z]+[^\S]+[0-9]+[^\S]+[0-9]+:[0-9]+:[0-9]+)[^\S]+([^\s]+)[^\]]+\]\:[^\S]+(UI_CMDLINE_READ_LINE)\:[^\S]+[^\s]+[^\S]+\'([^\']+)\'\,[^\S]+[^\s]+[^\S]+\'(run[^\']+|show[^\']+)"
    return data


def RPD_RSVP_NBRDOWN() -> str:
    data = "([a-zA-Z]+[^\S]+[0-9]+[^\S]+[0-9]+:[0-9]+:[0-9]+)[^\S]+([^\s]+)[^\S]+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\:.*(RPD_RSVP_NBRDOWN)\:[^\S]+[^\s]+[^\S]+[^\s]+[^\S]+([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}).*(down).*interface[^\S]+([^\s]+)[^\S]+[^\s]+[^\S]+([^\,]+)\,[^\S]+.*"
    return data


def RPD_RSVP_NBRUP() -> str:
    data = "([a-zA-Z]+[^\S]+[0-9]+[^\S]+[0-9]+:[0-9]+:[0-9]+)[^\S]+([^\s]+)[^\S]+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\:.*(RPD_RSVP_NBRUP)\:.*neighbor[^\S]+([^\s]+)[^\S]+([^\s]+)[^\S]+[^\s]+[^\S]+[^\s]+[^\S]+([^\s]+)[^\S]+[^\s]+[^\S]+([^\s]+)"
    return data


def SNMP_EVLIB_FAILURE() -> str:
    data = "([a-zA-Z]+[^\S]+[0-9]+[^\S]+[0-9]+:[0-9]+:[0-9]+)[^\S]+([^\s]+)[^\S]+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\:.*(SNMP_EVLIB_FAILURE)\:[^\S]+(.*stats)\.[^\S]+(.*)"
    return data


def Connection_to_RE() -> str:
    data = "([a-zA-Z]+[^\S]+[0-9]+[^\S]+[0-9]+:[0-9]+:[0-9]+)[^\S]+([^\s]+)[^\S]+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\:[^\S]+\(([^\)]+)\)[^\S]+([^\s]+)[^\:]+\:[^\S]+(?:MSPSMD_RE_CONN_PROGRESS\:[^\S]+[^\:]+\:[^\S]+|).*(RE).*(reconnect|progress).*"
    return data


def Connection_to_SPD_Failed() -> str:
    data = "([a-zA-Z]+[^\S]+[0-9]+[^\S]+[0-9]+:[0-9]+:[0-9]+)[^\S]+([^\s]+)[^\S]+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\:[^\S]+\(([^\)]+)\)[^\S]+([^\s]+).*(SPD).*(reconnect)"
    return data


def DDOS_PROTOCOL_VIOLATION_SET() -> str:
    data = "([a-zA-Z]+[^\S]+[0-9]+[^\S]+[0-9]+:[0-9]+:[0-9]+)[^\S]+([^\s]+)[^\S]+([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})[^\]]+\]\:[^\S]+(DDOS_PROTOCOL_VIOLATION_SET)\:[^\:]+\:.*protocol\/exception[^\S]+([^\s]+).*bandwidth[^\S]+[^\s]+[^\S]+([^\s]+[^\S]+[^\s]+)[^\S]+[^\s]+[^\S]+([^\s]+).*at[^\S]+([^\s]+[^\S]+[^\s]+)[^\S]+([^\s]+)"
    return data


def DDOS_PROTOCOL_VIOLATION_CLEAR() -> str:
    data = "([a-zA-Z]+[^\S]+[0-9]+[^\S]+[0-9]+:[0-9]+:[0-9]+)[^\S]+([^\s]+)[^\S]+([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})[^\]]+\]\:[^\S]+(DDOS_PROTOCOL_VIOLATION_CLEAR)\:[^\:]+\:.*protocol\/exception[^\S]+([^\s]+).*exceeded[^\S]+[^\s]+[^\S]+([^\s]+[^\S]+[^\s]+)[^\S]+[^\s]+[^\S]+([^\s]+).*from[^\S]+([^\s]+[^\S]+[^\s]+).*to[^\S]+([^\s]+[^\S]+[^\s]+)[^\S]+([^\s]+)"
    return data


def LOGIN_PAM_AUTHENTICATION_ERROR() -> str:
    data = "([a-zA-Z]+[^\S]+[0-9]+[^\S]+[0-9]+:[0-9]+:[0-9]+)[^\S]+([^\s]+)[^\S]+([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})[^\]]+\]\:[^\S]+(LOGIN_PAM_AUTHENTICATION_ERROR)\:.*user[^\S]+([^\s]+)"
    return data


def LOGIN_INFORMATION() -> str:
    data = "([a-zA-Z]+[^\S]+[0-9]+[^\S]+[0-9]+:[0-9]+:[0-9]+)[^\S]+([^\s]+)[^\S]+([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})[^\]]+\]\:[^\S]+(LOGIN_INFORMATION)\:.*User[^\S]+([^\s]+).*host[^\S]+([^\s]+).*device[^\S]+([^\s]+)"
    return data


def LOGIN_FAILED() -> str:
    data = "([a-zA-Z]+[^\S]+\d+[^\S]+[0-9]+:[0-9]+:[0-9]+)[^\S]+([^\s]+)[^\S]+([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})\:.*\:[^\S]+(LOGIN_FAILED).*user[^\S]+(?:\'|)(\w+).*host[^\S]+(?:\'|)([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})"
    return data


def SSHD_LOGIN_FAILED() -> str:
    data = "([a-zA-Z]+[^\S]+\d+[^\S]+[0-9]+:[0-9]+:[0-9]+)[^\S]+([^\s]+)[^\S]+([^\:]+)\:.*\:[^\S]+(SSHD_LOGIN_FAILED).*user[^\S]+(?:\'|)(\w+).*host[^\S]+(?:\'|)([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})"
    return data


def RPD_MPLS_PATH_DOWN() -> str:
    data = "([a-zA-Z]+[^\S]+[0-9]+[^\S]+[0-9]+:[0-9]+:[0-9]+)[^\S]+([^\s]+)[^\S]+([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}).*(RPD_MPLS_PATH_DOWN)\:.*path[^\S]+([^\s]+)[^\S]+(down)[^\S]+[^\s]+[^\S]+(LSP.*)"
    return data


def RPD_MPLS_PATH_UP() -> str:
    data = "([a-zA-Z]+[^\S]+[0-9]+[^\S]+[0-9]+:[0-9]+:[0-9]+)[^\S]+([^\s]+)[^\S]+([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}).*(RPD_MPLS_PATH_UP)\:[^\S]+[^\s]+[^\S]+[^\s]+[^\S]+([^\s]+)[^\S]+(up)[^\S]+[^\s]+[^\S]+([^\s]+[^\S]+[^\s]+)[^\S]+[^\s]+[^\S]+[^\s]+[^\S]+(.*)bps"
    return data


def PAM_SSHD() -> str:
    data = "([a-zA-Z]+[^\S]+\d+[^\S]+[0-9]+:[0-9]+:[0-9]+)[^\S]+([^\s]+)[^\S]+([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})\:.*(PAM).*error[^\S]+for[^\S]+([^\s]+).*from[^\S]+([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})"
    return data

def jun_Temperature() -> str:
    data = "([a-zA-Z]+[^\S]+\d+ \d+:\d+:\d+) ([^\s]+) (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):[^:]+:[^:]+:[^:]+: ([^\!]+)\![^:]+: ([^\s]+)[^\,]+\, [^\s]+ (\d+)"
    return data
