
class Migrations(object):

    def upgrade(self, version=0):
        return "Starting migration up!"

    def downgrade(self, version=0):
        print "Starting migration down!"
