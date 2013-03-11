# -*- coding: utf-8 -*-

import pymigrations
import inspect

from os.path import basename
from pymigrations import conf
from importlib import import_module
from modulefinder import ModuleFinder


class DiscovererMigration(object):

    def __init__(self, execute=True, version_to=None, **kwargs):
        self.execute = execute
        self.version_to = version_to
        self.current_version = Version().get_current()

    def down_migrations(self, version=0):
        for migration_file in self.migrations_files(reverse=True):
            migration = MigrationWrapper(migration_file,  execute=self.execute)
            if migration.version <= self.current_version:
                yield migration

    def up_migrations(self, version=0):
        for migration_file in self.migrations_files():
            migration =  MigrationWrapper(migration_file,  execute=self.execute)
            if migration.version > self.current_version:
                yield migration

    def migrations_files(self, reverse=False):
        finder = ModuleFinder()
        submodules_names = finder.find_all_submodules(pymigrations)
        submodules_names.remove("conf")
        submodules = [import_module("pymigrations.%s" % name) for name in submodules_names]
        submodules = sorted(submodules, key=lambda s: s.version, reverse=reverse)
        return submodules

    def to_migrations(self):
        reverse = self.is_down()
        for migration_file in self.migrations_files(reverse):
            migration = MigrationWrapper(migration_file, execute=self.execute)
            if self.is_up():
                if self.current_version < migration.version <= self.version_to:
                    yield migration
            if self.is_down():
                if self.current_version >= migration.version > self.version_to:
                    yield migration

    def is_up(self):
        return self.version_to > self.current_version

    def is_down(self):
        return self.version_to < self.current_version


class MigrationWrapper(object):

    def __init__(self, migration_file, execute=True):
        self.migration_file = migration_file
        self.execute = execute

    def __repr__(self):
        return self.filename()

    def __eq__(self, migration):
        return self.migration_file == migration.migration_file

    def up(self):
        if self.execute:
            self.migration_file.up()

    def down(self):
        if self.execute:
            self.migration_file.down()

    def header(self):
        return inspect.getdoc(self.migration_file)

    def doc_up(self):
        return inspect.getdoc(self.migration_file.up)

    def doc_down(self):
        return inspect.getdoc(self.migration_file.down)

    @property
    def version(self):
        return self.migration_file.version

    def filename(self):
        return basename(self.migration_file.__file__.replace('.pyc', '.py'))


class Version(object):

    def set_current(self, version):
        if getattr(conf, "set_current_version", None):
            return conf.set_current_version()
        else:
            path = "%s/current_version.txt" % conf.folder
            with open(path, "w") as f:
                content = f.write(version)
            return content

    def get_current(self):
        if getattr(conf, "current_version", None):
            return conf.current_version()
        else:
            path = "%s/current_version.txt" % conf.folder
            with open(path, "r+") as f:
                content = f.read()
            return content
    