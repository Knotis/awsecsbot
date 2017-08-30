class ServiceProviderCommandNotImplemented(Exception):
    message_template = (
        'The command%s is not supported by service provider%s.'
    )
    def __init__(
        self,
        provider_name='',
        command_name='',
        *args,
        **kwargs
    ):
        super(ServiceProviderCommandNotImplemented, self).__init__(
            *args,
            **kwargs
        )

        if '' != provider_name and '' != command_name:
            self.message = self.message_template % (
                ' ' + command_name,
                ' ' + provider_name
            )

class ProviderBase(object):
    provider = ''  # Set provider name here as a string.

    def up(self):
        '''
        Build and run a local version of your containers.
        '''
        raise ServiceProviderCommandNotImplemented(
            provider_name=self.provider,
            command_name='up'
        )

    def down(self):
        '''
        Destroy local containers.
        '''
        raise ServiceProviderCommandNotImplemented(
            provider_name=self.provider,
            command_name='down'
        )

    def deploy(self):
        '''
        Build and deploy a new version of your
        containers to a remote environment.
        '''
        raise ServiceProviderCommandNotImplemented(
            provider_name=self.provider,
            command_name='deploy'
        )

    def stop(self):
        '''
        Stop running container instances.
        '''
        raise ServiceProviderCommandNotImplemented(
            provider_name=self.provider,
            command_name='stop'
        )

    def configure(self):
        '''
        Configure the current environment for the specified
        deployment stage.
        '''
        raise ServiceProviderCommandNotImplemented(
            provider_name=self.provider,
            command_name='configure'
        )

    def version(self):
        '''
        Modifies the local configuration incrementing the
        current version number. 
        '''
        raise ServiceProviderCommandNotImplemented(
            provider_name=self.provider,
            command_name='version'
        )

    def commit_environment(self):
        '''
        Commits local configuration files to the remote location
        configured for the current deployment.
        '''
        raise ServiceProviderCommandNotImplemented(
            provider_name=self.provider,
            command_name='commit-environment'
        )

    def create(self):
        '''
        Create resources on the service provider required
        for deployment.
        '''
        raise ServiceProviderCommandNotImplemented(
            provider_name=self.provider,
            command_name='create'
        )

    def destroy(self):
        '''
        Destroy the deployment for the current environent
        and remove all resources from service provider.
        '''
        raise ServiceProviderCommandNotImplemented(
            provider_name=self.provider,
            command_name='destroy'
        )

    def test(self):
        '''
        Run the test docker container provided.
        '''
        raise ServiceProviderCommandNotImplemented(
            provider_name=self.provider,
            command_name='test'
        )
