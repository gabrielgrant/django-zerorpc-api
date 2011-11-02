import datetime
import decimal

from django.core.serializers import python
from django.utils import datetime_safe
from django.utils.encoding import is_protected_type

class Serializer(python.Serializer):
    def handle_field(self, obj, field):
        value = field._get_val_from_obj(obj)
        value = coerce_datetime(value)
        if is_protected_type(value):
            self._current[field.name] = value
        else:
            self._current[field.name] = field.value_to_string(obj)


DATE_FORMAT = "%Y-%m-%d"
TIME_FORMAT = "%H:%M:%S"

def coerce_datetime(o):
    if isinstance(o, datetime.datetime):
        d = datetime_safe.new_datetime(o)
        return d.strftime("%s %s" % (DATE_FORMAT, TIME_FORMAT))
    elif isinstance(o, datetime.date):
        d = datetime_safe.new_date(o)
        return d.strftime(DATE_FORMAT)
    elif isinstance(o, datetime.time):
        return o.strftime(TIME_FORMAT)
    elif isinstance(o, decimal.Decimal):
        return str(o)
    else:
        return o
