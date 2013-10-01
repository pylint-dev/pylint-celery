from astroid import MANAGER
from astroid.builder import AstroidBuilder
from astroid import nodes


MODULE_TRANSFORMS = {}


def transform(module):
    try:
        tr = MODULE_TRANSFORMS[module.name]
    except KeyError:
        pass
    else:
        tr(module)
MANAGER.register_transform(nodes.Module, transform)


def celery_transform(module):
    fake = AstroidBuilder(MANAGER).string_build('''
class task_dummy(object): pass
''')
    module.locals['task'] = fake.locals['task_dummy']


MODULE_TRANSFORMS['celery'] = celery_transform