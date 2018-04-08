# -*- coding: utf-8 -*-
"""
    lantz.sims.config
    ~~~~~~~~~~~~~~~~~

    :copyright: 2018 by The Lantz Authors
    :license: BSD, see LICENSE for more details.
"""


from lantz_core.config import register_and_get


# ====================================
# Configuration Values for lantz_sims
# ====================================

TCP_HOST = register_and_get('sims.tcp_host', 'localhost')
TCP_PORT = int(register_and_get('sims.tcp_port', '5678'))
