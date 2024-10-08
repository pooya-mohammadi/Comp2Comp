"""
@author: louisblankemeier
"""

from typing import Dict


class InferenceClass:
    """Base class for inference classes."""

    def __call__(self, inference_pipeline) -> Dict:
        raise NotImplementedError

    def __repr__(self):
        return self.__class__.__name__
