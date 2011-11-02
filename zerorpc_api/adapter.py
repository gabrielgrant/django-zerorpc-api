from django.core import serializers
from . import utils

def get(model_label, params):
    """get a single instance of a django model with the given params
    
    model_label - string containing "app_label.model_name"
    params - JSON object of query params
    
    example:
    
    >>> web3db.get('auth.User', {'id': 23})
    """
    model = utils._get_model(model_label)
    obj = model.objects.get(**params)
    return serializers.serialize('python', [obj])[0]
    
_query_stage_type_map = {
    'filter': lambda x: x.filter,
    'exclude': lambda x: x.exclude,
}

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
    
    """
    model = utils._get_model(model_label)
    qs = model.objects.all()
    for stage in query_stages:
        qs = _query_stage_type_map[stage['type']](qs)(**stage['params'])
    return serializers.serialize('python', qs)


