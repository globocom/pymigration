import os


class Migrations(object):

    def upgrade(self, version=0):
        print "Starting migration up!"

    def downgrade(self, version=0):
        print "Starting migration down!"




def fullpath(*args):
    project_path = os.path.dirname(__file__)
    return os.path.abspath(os.path.join(project_path, '..', *args))
