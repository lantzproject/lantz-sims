
import copy

from lantz.core.mfeats import MFeatMixin, DictMFeatMixin


def build_feat_simulator(feat_name):

    class FeatSimulator:

        @staticmethod
        def get(inst):
            return inst.sim_values[feat_name]

        @staticmethod
        def set(inst, value):
            inst.sim_values[feat_name] = value

    return FeatSimulator


def build_dictfeat_simulator(feat_name):

    def using(key):

        class DictFeatSimulator:

            @staticmethod
            def get(inst):
                return inst.sim_values[feat_name][key]

            @staticmethod
            def set(inst, value):
                inst.sim_values[feat_name][key] = value

        return DictFeatSimulator

    return using


def build_local_action(action_name):

    def call(inst, *args, **kwargs):
        return inst.sim_values[action_name]

    return call


def wrap_driver_cls(wrapped_cls, initial_values=None):

    ORIGINAL_SUFFIX = '_nosim_'

    initial_values = initial_values or {}

    class WrappedCLS(wrapped_cls):

        def initialize(self):
            self.sim_values = copy.deepcopy(initial_values)
            super().initialize()

    for feat_name in wrapped_cls._lantz_feats.keys():
        feat = getattr(wrapped_cls, feat_name)
        feat._simulator = build_feat_simulator(feat_name)

        if isinstance(feat, MFeatMixin):
            if feat_name not in initial_values:
                initial_values[feat_name] = feat.get_initial_value()

    for feat_name in wrapped_cls._lantz_dictfeats.keys():
        feat = getattr(wrapped_cls, feat_name)
        feat._simulator = build_dictfeat_simulator(feat_name)

        if isinstance(feat, DictMFeatMixin):
            if feat_name not in initial_values:
                initial_values[feat_name] = feat.get_initial_value()
            else:
                initial_values[feat_name] = dict(feat.get_initial_value(), **initial_values[feat_name])

    for action_name in wrapped_cls._lantz_actions.keys():
        if action_name in ('initialize', 'finalize', 'initialize_async', 'finalize_async',
                           'update', 'refresh', 'update_async', 'refresh_async'):
            continue

        # if action_name.endswith('_async'):
        #     continue
        getattr(WrappedCLS, action_name)._simulator = build_local_action(action_name)


    WrappedCLS.__name__ = 'Sim' + wrapped_cls.__name__

    return WrappedCLS
