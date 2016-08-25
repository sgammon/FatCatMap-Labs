from momentum.fatcatmap.core.struct import FCMStructure
from ProvidenceClarity.struct.rpc import RPCRequestStructure
from ProvidenceClarity.struct.rpc import RPCResponseStructure


class FCM_RPCRequestStructure(FCMStructure, RPCRequestStructure):
	pass


class FCM_RPCResponseStructure(FCMStructure, RPCResponseStructure):
	pass