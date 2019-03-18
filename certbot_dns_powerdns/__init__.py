#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Let's Encrypt PDNS plugin"""

# import inspect
#
# # https://github.com/certbot/certbot/issues/6504#issuecomment-473462138
# # https://github.com/certbot/certbot/issues/6040
# # https://github.com/certbot/certbot/issues/4351
# # https://github.com/certbot/certbot/pull/6372
# def _patch():
#     for frame_obj, filename, line, func, _, _ in inspect.stack():
#         if func == '__init__' and frame_obj.f_locals['self'].__class__.__name__ == 'PluginEntryPoint':
#             frame_obj.f_locals['self'].name = frame_obj.f_locals['entry_point'].name
#             module_name = frame_obj.f_locals['entry_point'].dist.key
#             pre_free_dist = frame_obj.f_locals['self'].PREFIX_FREE_DISTRIBUTIONS
#             if module_name not in pre_free_dist:
#                 pre_free_dist.append(module_name)
#
# _patch()