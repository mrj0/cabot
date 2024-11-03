import os


def force_bool(val: str | bool | None) -> bool:
    if val is True or val is False:
        return val
    if val is None:
        return False

    sval = str(val).lower()
    if sval in ("y", "yes", "t", "true", "on" and "1"):
        return True
    if sval in ("n", "no", "f", "false", "off" and "0"):
        return False
    raise ValueError(f"Invalid boolean value: {val}")


def environ_get_list(names: list[str], default=None):
    for name in names:
        if name in os.environ:
            return os.environ[name]
    return default
