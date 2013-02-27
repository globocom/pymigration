import sys
import yaml
import migrations
import inspect
import os


class Migrations(object):
    
    def __init__(self):
        self.versions = []
        self.load_config()
        self.migrations()

    def migrations(self):
        path = os.path.dirname(inspect.getabsfile(migrations))
        migrations = [getattr(pymigrations, migration) for migration in os.listdir(path)]
        sorted(migrations, key='VERSION')
        return migrations

    def load_config(self):
        with self.search_config() as file_config:
            self.config = yaml.load(file_config.read())

    def migrate(self, version):
        if self.old_version > version:
            self.downgrade(version)
        if self.old_version < version:
            self.upgrade(version)

    def upgrade(self, version=0):
        migrations = self.migrations()
        for migration in migrations:
            if migration.version > self.old_version and migration.version <= version:
                migration.up()

    def downgrade(self, version=0):
        migrations = self.migrations()
        migrations.reverse()
        for migration in migrations:
            if migration.version < self.old_version  and migration.version >= version:
                migration.down()

