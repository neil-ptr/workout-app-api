from sqlalchemy import inspect

def object_as_dict(obj):
    """ convert sqlalchemy query object to a python dict

    Args:
        obj: sqlalchemy query object

    Returns:
        dict
    """
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}