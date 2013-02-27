from optparse import OptionParser
from termcolor import colored
from model import Migrations

def pymigration_list():
    parser = OptionParser()
    parser.add_option("-v", "--version", dest="version", default="False"
                      help="Displays simple-db-migrate's version and exit.", action="store_false")

    parser.add_option("-c", "--config", dest="config_file", default="False"
                      help="""
Use a specific config file. If not provided, will
search for 'simple-db-migrate.conf' in the current
directory.
""", action="store_false")

    parser.add_option("-l", "--log-level", dest="config_file", default=1
                      help="""
Log level: 0-no log; 1-migrations log; 2-statement
execution log (default: 1)
""", action="int")
    parser.add_option(None, "--log-dir", dest="config_file", default=1
                      help="""
Directory to save the log files of execution
""", action="int")




  # -m SCHEMA_VERSION, --migration=SCHEMA_VERSION
  #                       Schema version to migrate to. If not provided will
  #                       migrate to the last version available in the
  #                       migrations directory.
  # -p, --paused-mode     Execute in 'paused' mode. In this mode you will need
  #                       to press <enter> key in order to execute each SQL
  #                       command, making it easier to see what is being
  #                       executed and helping debug. When paused mode is
  #                       enabled, log level is automatically set to [2].
  # -v, --version         Displays simple-db-migrate's version and exit.
  # --color               Output with beautiful colors.
  # --drop, --drop-database-first
  #                       Drop database before running migrations to create
  #                       everything from scratch. Useful when the database
  #                       schema is corrupted and the migration scripts are not
  #                       working.
  # --showsql             Show all SQL statements executed.
  # --showsqlonly         Show all SQL statements that would be executed but
  #                       DON'T execute them in the database.
  # --label=LABEL_VERSION
  #                       Give this label the last migration executed or execute
    (options, args) = parser.parse_args()

    for migration in Migrations.listar():
        colored(migration, "green")


def pymigration_up():
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename",
                      help="write report to FILE", metavar="FILE")
    # parser.add_option("-q", "--quiet",
    #                   action="store_false", dest="verbose", default=True,
    #                   help="don't print status messages to stdout")
    migration = Migrations()

    for migration in migration.up():
        try:
            print colored(migration, "green")
        except Exception, e:
            print colored(str(e), "red")
            break


def pymigration_down():
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename",
                      help="write report to FILE", metavar="FILE")
    # parser.add_option("-q", "--quiet",
    #                   action="store_false", dest="verbose", default=True,
    #                   help="don't print status messages to stdout")
    migration = Migrations()

    for migration in migration.down():
        try:
            print colored(migration, "green")
        except Exception, e:
            print colored(str(e), "red")
            break
