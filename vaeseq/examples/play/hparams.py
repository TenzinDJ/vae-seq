"""Hyperparameters for this example."""

from vaeseq import hparams as hparams_mod

_DEFAULTS = dict(
    latent_size=16,
    sequence_size=40,
    obs_encoder_fc_layers=[32, 32],
    obs_decoder_fc_hidden_layers=[32],
    latent_decoder_fc_layers=[32],
    rnn_hidden_sizes=[32],
    game="CartPole-v0",
    game_output_size=[4],
    game_action_space=2,
    train_agent=True,
)


def make_hparams(flag_value=None, **kwargs):
    """Initialize HParams with the defaults in this module."""
    init = dict(_DEFAULTS)
    init.update(kwargs)
    ret = hparams_mod.make_hparams(flag_value=flag_value, **init)
    return ret