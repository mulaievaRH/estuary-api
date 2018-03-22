# SPDX-License-Identifier: GPL-3.0+


class BaseScraper(object):
    """
    Base scraper class to standardize the main scraper functionality
    """
    def run(self, since=None):
        """
        Run the scraper
        :kwarg since: a string of a UTC timestamp in the ISO 8601 format or
        a datetime object
        :return: None
        """
        raise NotImplementedError()
