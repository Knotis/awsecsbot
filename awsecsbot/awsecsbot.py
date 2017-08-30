class AwsecsBotApplication(object):
    def run(
        self,
        *args,
        **kwargs
    ):
        pass

app = None
def run(
    *args,
    **kwargs
):
    if None is app:
        app = AwsecsBotApplication(*args, **kwargs)

    app.run()
