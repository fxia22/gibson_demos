from gibson2.object_states.object_state_base import CachingEnabledObjectState
import numpy as np


class Pose(CachingEnabledObjectState):

    def _compute_value(self):
        pos = self.obj.get_position()
        orn = self.obj.get_orientation()
        return np.array(pos), np.array(orn)

    def _set_value(self, new_value):
        raise NotImplementedError("Pose state currently does not support setting.")

    # Nothing needs to be done to save/load Pose since it will happen due to pose caching.
    def _dump(self):
        return None

    def _load(self, data):
        return