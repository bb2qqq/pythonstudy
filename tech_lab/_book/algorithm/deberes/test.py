def nested_depth(target):
    if not isinstance(target, dict):
        return 0
    if not target:
        return 1
    return 1 + max(nested_depth(v) for v in target.values())
