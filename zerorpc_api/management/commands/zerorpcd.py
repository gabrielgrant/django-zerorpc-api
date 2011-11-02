import sys

from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from ... import adapter

import zerorpc

class Command(BaseCommand):
    help = "Runs a ZeroRPC server providing access to Django models."
    #args = "<userid|username> <product_name>"

    def handle(self, *args, **options):
        try:
            port = settings.ZERORPC_PORT
        except AttributeError:
            e = CommandError('No port specified (in "ZERORPC_PORT" setting)')
            raise e, None, sys.exc_info()[2]
        server = zerorpc.Server(methods=adapter)
        self.stdout.write('\n\n\Binding to port %s...' % port)
        server.bind('tcp://0:%s' % port)
        self.stdout.write('\n\nRunning server...\n\n')
        server.run()


