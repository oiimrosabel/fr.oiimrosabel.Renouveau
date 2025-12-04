from gi.repository import GObject


class UpdateState(GObject.GEnum):
    __gtype_name__ = "UpdateState"

    HIDDEN = 0
    SCHEDULED = 1
    ONGOING = 2
    SUCCESS = 3
    FAIL = 4
