from collections import defaultdict
from dimensions_extractors import DimensionExtractor
from models import LogEntry


class StatisticsAggregator:

    def __init__(self, extractors: list[DimensionExtractor]):
        self.extractors = extractors
        self.counts = {
            extractor.name: defaultdict(int)
            for extractor in extractors
        }
        self.total = 0

    def process(self, log_entry: LogEntry):
        self.total += 1
        for extractor in self.extractors:
            value = extractor.extract(log_entry)
            self.counts[extractor.name][value] += 1
