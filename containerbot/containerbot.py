import click

from .awsecs import AwsEcs


class ServiceProviderNotSuportedException(Exception):
    message = 'The service provider selected is not supported.'


@click.command()
@click.argument('command')
@click.option(
    '--docker-compose-file',
    '-f',
    default='./docker-compose.yml',
    help='Location of the docker-compose.yml file to use for this deployment.'
)
@click.option(
    '--service-provider',
    '-P',
    default='aws',
    help='The service provider who will be hosting your containers.',
)
def run(
    command,
    docker_compose_file,
    service_provider,
    *args,
    **kwargs
):
    if 'aws' == service_provider:
        command_interface = AwsEcs()

    else:
        raise ServiceProviderNotSuportedException()
    '''
    This tool is designed to manage and deploy docker containers to AWS ECS and other container hosting services.
    '''
    pass
