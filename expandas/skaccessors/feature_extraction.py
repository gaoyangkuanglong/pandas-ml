#!/usr/bin/env python

import numpy as np
import pandas as pd
from pandas.util.decorators import cache_readonly

from expandas.core.accessor import AccessorMethods


class FeatureExtractionMethods(AccessorMethods):
    """
    Accessor to ``sklearn.feature_extraction``.
    """

    _module_name = 'sklearn.feature_extraction'

    # image

    @property
    def image(self):
        """Property to access ``sklearn.feature_extraction.image``"""
        return self._image

    @cache_readonly
    def _image(self):
        return AccessorMethods(self._df, module_name='sklearn.feature_extraction.image')

    # text

    @property
    def text(self):
        """Property to access ``sklearn.feature_extraction.text``"""
        return self._text

    @cache_readonly
    def text(self):
        attrs = ['CountVectorizer', 'HashingVectorizer',
                 'TfidfTransformer', 'TfidfVectorizer']
        return AccessorMethods(self._df, module_name='sklearn.feature_extraction.text',
                               attrs=attrs)


