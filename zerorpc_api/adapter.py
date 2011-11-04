from .serializer import Serializer
from . import utils

def serialize(*args, **kwargs):
    single = kwargs.get('single', False)
    # this should be def serialize(*args, single=False):
    s = Serializer()
    def middle(f):
        def inner(*args, **kwargs):
            if single:
                ret = f(*args, **kwargs)
                if ret is None:
                    return
                else:
                    return s.serialize([ret])[0]
            else:
                return s.serialize(f(*args, **kwargs))
        return inner
    if args:
        return middle(args[0])
    else:
        return middle

@serialize(single=True)
def get(model_label, params):
    """get a single instance of a django model with the given params
    
    model_label - string containing "app_label.model_name"
    params - JSON object of query params
    
    example:
    
    >>> web3db.get('auth.User', {'id': 23})
    
    $ zerorpc-client --json tcp://0:5555 get '"auth.User"' {"id": 1}'
    """
    model = utils._get_model(model_label)
    try:
        obj = model.objects.get(**params)
    except model.DoesNotExist:
        obj = None
    return obj
    
_query_stage_type_map = {
    'filter': lambda x: x.filter,
    'exclude': lambda x: x.exclude,
}

@serialize
def query(model_label, query_stages):
    """get a list of instances matching the given query params
    
    model_label - string containing "app_label.model_name"
    query_stages - list of JSON objects holding query params
    
    example:
    
    >>> web3db.query('auth.User', [
    ...     {type: 'filter', params: {'name__startswith': 'G'}},
    ...     {type: 'exclude', params: {'id__lt': 25}},
    ... ])
    ...
    
    $ zerorpc-client --json tcp://0:5555 query '"auth.User"' '[
        {"type":"filter", "params":{"id": 1}}
    ]'
    
    """
    model = utils._get_model(model_label)
    qs = model.objects.all()
    for stage in query_stages:
        qs_type = _query_stage_type_map[stage['type']](qs)
        qs = qs_type(**stage['params'])
    return qs


