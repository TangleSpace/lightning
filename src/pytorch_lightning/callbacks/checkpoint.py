from pytorch_lightning.callbacks.callback import Callback


class Checkpoint(Callback):
    r"""
    This is the base class for Model checkpointing. Expert users may want to subclass it in case of writing
    custom :class:`~pytorch_lightning.callbacks.model_checkpoint.ModelCheckpoint` callback, so that
    the trainer recognizes the custom class as a checkpointing callback.
    """