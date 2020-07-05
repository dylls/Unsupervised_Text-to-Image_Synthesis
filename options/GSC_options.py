#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base_options import BaseOptions

class DAMSMOptions(BaseOptions):
    def initialize(self):
        BaseOptions.initialize(self)

        # TREE
        self._parser.add_argument('--BRANCH_NUM', type=int, default=1)
        self._parser.add_argument('--BASE_SIZE', type=int, default=299)

        # TRAIN
        self._parser.add_argument('--FLAG', action='store_false')
        self._parser.add_argument('--NET_G', type=str, default='')
        self._parser.add_argument('--B_NET_D', action='store_false')

        self._parser.add_argument('--DISCRIMINATOR_LR', type=float, default=0.0002)
        self._parser.add_argument('--GENERATOR_LR', type=float, default=0.0002)

        self._parser.add_argument('--NET_E', type=str, default='')
        self._parser.add_argument('--MAX_EPOCH', type=int, default=600)
        self._parser.add_argument('--SNAPSHOT_INTERVAL', type=int, default=5)
        self._parser.add_argument('--GAMMA1', type=float, default=4.0)
        self._parser.add_argument('--GAMMA2', type=float, default=5.0)
        self._parser.add_argument('--GAMMA3', type=float, default=10.0)
        self._parser.add_argument('--LAMBDA', type=float, default=50.0)

        # TEXT
        self._parser.add_argument('--EMBEDDING_DIM', type=int, default=256)
        self._parser.add_argument('--CAPTIONS_PER_IMAGE', type=int, default=1)
        self._parser.add_argument('WORDs_NUM', type=int, default=15)
