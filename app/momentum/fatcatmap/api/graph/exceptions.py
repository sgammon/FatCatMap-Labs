from momentum.fatcatmap.api.exceptions import ServiceException


class GraphAPIException(ServiceException): pass
class NodeNotFound(GraphAPIException): pass