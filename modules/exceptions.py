class TransportError(Exception):
    """Error on the transport layer"""

class SQLStorageExecutionError(Exception):
    """Error during the execution SQL script"""

class SendAliveError(Exception):
    """Error during the execution SQL script"""

class NoProxiesError(Exception):
    """you have to setup proxies"""

class WrongStorageTypeError(Exception):
    """wrong (unidentified) storage's type"""

class WrongCrawlerTypeError(Exception):
    """wrong (unidentified) crawler's type"""

class MissingConfigKeyError(Exception):
    """config's key not found"""
