import _plotly_utils.basevalidators


class TextValidator(_plotly_utils.basevalidators.StringValidator):

    def __init__(
        self, plotly_name='text', parent_name='layout.yaxis.title', **kwargs
    ):
        super(TextValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'ticks'),
            role=kwargs.pop('role', 'info'),
            **kwargs
        )