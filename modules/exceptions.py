class TransportError(Exception):
    """Error on the transport layer"""
    pass

class SQLStorageExecutionError(Exception):
    """Error during the execution SQL script"""
    pass

class SendAliveError(Exception):
    """Error during the execution SQL script"""
    pass

class NoProxiesError(Exception):
    """you have to setup proxies"""
    pass

class WrongStorageTypeError(Exception):
    """wrong (unidentified) storage's type"""
    pass

class WrongCrawlerTypeError(Exception):
    """wrong (unidentified) crawler's type"""
    pass

class MissingConfigKeyError(Exception):
    """config's key not found"""
    pass
