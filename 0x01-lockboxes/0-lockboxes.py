#!/usr/bin/env python3
"Lockboxes"


def canUnlockAll(boxes):
    "UnLock all boxes"
    keys = {0}
    unopened = []
    for idx, box in enumerate(boxes):
        if idx in keys:
            keys.update(box)
            keys.remove(idx)
        else:
            unopened.append(idx)

    for idx in unopened:
        if idx in keys:
            keys.update(boxes[idx])
            keys.remove(idx)
            unopened[unopened.index(idx)] = -1

    return len(unopened) == 0 or all(i == -1 for i in unopened)
