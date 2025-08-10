from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    
    help = 'Creates a new app using a custom template.'

    def add_arguments(self, parser):
        parser.add_argument('app_name', type=str, help='The name of the new app.')

    def handle(self, *args, **options):
        app_name = options['app_name']
        template_url = 'https://codeload.github.com/abhishek-0x49310/django-project-templates/zip/refs/heads/app-template-rest-framework'
        
        try:
            call_command(
                'startapp',
                app_name,
                f"--template={template_url}"
            )
        except Exception as e:
            raise CommandError(f"Error while creating app: {e}")
