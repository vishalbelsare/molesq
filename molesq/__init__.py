"""
# molesq package

A python implementation of the MOving LEast SQuares algorithm
for transforming sets of points from one space to another,
as published in [Schaefer et al. (2006)][1].

Adapted from [implementation by Casey Schneider-Mizell][2].

[1]: https://doi.org/10.1145/1179352.1141920
[2]: https://github.com/ceesem/catalysis/blob/master/catalysis/transform.py

"""
from .version import version as __version__  # noqa: F401
from .version import version_tuple as __version_info__  # noqa: F401

from .new import Strategy, Transformer

__all__ = ["Strategy", "Transformer"]