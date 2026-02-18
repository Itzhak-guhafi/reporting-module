from log_parser import parse_log_line
from dimensions_extractors import CountryExtractor, OSExtractor, BrowserExtractor
from aggregator import StatisticsAggregator
from reporter import generate_report
import geoip2.database

def main():
    log_file = "apache_log.txt"
    geoip_reader = geoip2.database.Reader("GeoLite2-Country.mmdb")

    # Dimensions extractors
    extractors = [
        CountryExtractor(geoip_reader),
        OSExtractor(),
        BrowserExtractor()
    ]

    # Aggregator
    aggregator = StatisticsAggregator(extractors)

    with open(log_file, "r", encoding="utf-8") as f:
        for line in f:
            entry = parse_log_line(line)
            aggregator.process(entry)

    geoip_reader.close()

    # Reporter
    generate_report(aggregator.counts, aggregator.total)

if __name__ == "__main__":
    main()