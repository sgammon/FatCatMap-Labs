from momentum.fatcatmap.api.exceptions import ServiceException


class DataAPIException(ServiceException): pass

class InvalidKey(DataAPIException): pass
class KeyNotFound(DataAPIException): pass


class MediaException(DataAPIException): pass

class InvalidMedia(MediaException): pass
class MediaNotFound(MediaException): pass