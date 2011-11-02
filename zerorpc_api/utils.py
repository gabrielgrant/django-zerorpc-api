from django.db.models.loading import get_model

def _get_model(model_label):
    if model_label.count('.') != 1:
        raise ValueError(
            'model_label is not a valid model label - '
            'it must be of the form "app_label.model_name"')
    app_label, model_name = model_label.split('.')
    model = get_model(app_label, model_name)
    return model
