from packagesloader.services import PackageParserService


def parse_and_load_feed():
    parsing_service = PackageParserService()
    parsed_packages = parsing_service.parse_packages_from_rss_source()
    y = ""