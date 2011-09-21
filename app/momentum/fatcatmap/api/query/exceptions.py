from momentum.fatcatmap.api.exceptions import ServiceException


class QueryAPIException(ServiceException): pass

class InvalidQuery(QueryAPIException): pass
class InvalidFilter(QueryAPIException): pass
class InvalidOrder(QueryAPIException): pass
class InvalidProperty(QueryAPIException): pass

class InternalQueryAPIException(QueryAPIException): pass