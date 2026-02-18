from abc import ABC, abstractmethod
from ua_parser import user_agent_parser
import geoip2.database
from models import LogEntry

class DimensionExtractor(ABC):

    @property
    def name(self):
        raise NotImplementedError()

    @abstractmethod
    def extract(self, log_entry: LogEntry) -> str:
        raise NotImplementedError()

def safe_extract(func, default="Unknown"):
    try:
        return func()
    except:
        return default


# --------- CountryExtractor ---------
class CountryExtractor(DimensionExtractor):
    def __init__(self, geoip_reader: geoip2.database.Reader):
        self.reader = geoip_reader

    @property
    def name(self):
        return "Country"

    def extract(self, log_entry: LogEntry):
        return safe_extract(lambda: self.reader.country(log_entry.ip).country.name or "Unknown")


# --------- OSExtractor ---------
class OSExtractor(DimensionExtractor):
    @property
    def name(self):
        return "OS"

    def extract(self, log_entry: LogEntry):
        return safe_extract(lambda: user_agent_parser.Parse(log_entry.user_agent)["os"]["family"] or "Unknown")


# --------- BrowserExtractor ---------
class BrowserExtractor(DimensionExtractor):
    @property
    def name(self):
        return "Browser"

    def extract(self, log_entry: LogEntry):
        return safe_extract(lambda: user_agent_parser.Parse(log_entry.user_agent)["user_agent"]["family"] or "Unknown")