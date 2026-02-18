from dataclasses import dataclass

@dataclass
class LogEntry:
    ip: str
    user_agent: str