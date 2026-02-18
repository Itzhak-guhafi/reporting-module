from models import LogEntry

def parse_log_line(line: str) -> LogEntry:
    parts = line.split('"')
    ip = line.split(" ")[0]
    user_agent = parts[-2] if len(parts) > 1 else ""
    return LogEntry(ip=ip, user_agent=user_agent)
