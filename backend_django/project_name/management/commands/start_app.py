from pathlib import Path
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

class Command(BaseCommand):
    
    help = 'Creates a new app in {{ project_name }}/apps/ using a custom template.'

    def add_arguments(self, parser):
        parser.add_argument('app_name', type=str, help='The name of the new app.')
        parser.add_argument(
            '--template-url',
            type=str,
            
            default='https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPO_NAME/archive/refs/heads/main.zip',
            help='URL to the GitHub .zip archive of your template repository.'
        )

    def handle(self, *args, **options):
        app_name = options['app_name']
        template_url = options['template_url']
        
        # Determine the destination directory for the new app.
        # This assumes your project structure is 'myproject/project_name/apps/'
        project_name_dir = settings.BASE_DIR / '{{ project_name }}'
        apps_dir = project_name_dir / 'apps'
        
        # Ensure the 'apps' directory exists
        apps_dir.mkdir(parents=True, exist_ok=True)
        (apps_dir / '__init__.py').touch()
        
        destination_path = apps_dir / app_name
        
        if destination_path.exists():
            raise CommandError(f"App '{app_name}' already exists at '{destination_path}'.")

        self.stdout.write(f"Creating app '{app_name}' from template...")
        
        
        try:
            call_command(
                'startapp',
                app_name,
                f"--template={template_url}",
                target=destination_path
            )
        except Exception as e:
            raise CommandError(f"Error while creating app: {e}")