import protorpc

from protorpc import messages
from protorpc.messages import Field
from protorpc.messages import Variant


class VariantField(Field):

	"""Field definition for integer values."""

	VARIANTS = frozenset([Variant.DOUBLE, Variant.FLOAT, Variant.BOOL,
						  Variant.INT64, Variant.UINT64, Variant.SINT64,
						  Variant.INT32, Variant.UINT32, Variant.SINT32,
						  Variant.STRING, Variant.MESSAGE, Variant.BYTES, Variant.ENUM])

	DEFAULT_VARIANT = Variant.STRING

	type = (int, long, bool, basestring, dict, messages.Message)