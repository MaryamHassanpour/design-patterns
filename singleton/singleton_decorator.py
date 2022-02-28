# Implementing Singleton with decorator

def singleton(class_name):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_name not in instances:
            instances[class_name] = class_name(*args, **kwargs)
        return instances[class_name]

    return get_instance


@singleton
class SingletonClass:
    pass
