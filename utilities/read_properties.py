import configparser

config = configparser.RawConfigParser()
config.read("./configurations/config.ini")


class ReadConfig:
    @staticmethod
    def get_base_url():
        url = config.get('common data', 'baseUrl')
        return url

    @staticmethod
    def get_username():
        username = config.get('common data', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('common data', 'password')
        return password

    @staticmethod
    def get_search_item():
        item = config.get('common data', 'search_item')
        return item

    @staticmethod
    def get_match_item():
        item = config.get('common data', 'match_item')
        return item
