from momentum.core.model import db, ndb
from momentum.core.model import MomentumModel
from momentum.core.model import MomentumNDBModel
from momentum.core.model import property_classes
from momentum.core.model import MomentumPolymorphicModel


###### ====== Root Models ====== ######

## DB/Old Style Model
class FCMModel(MomentumModel):
	pass
	

## NDB/New Style Model
class NDBModel(MomentumNDBModel):
	pass
	

## PolyModel
FCMPolyModel = MomentumPolymorphicModel