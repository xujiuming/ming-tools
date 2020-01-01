import psutil


def mem():
    return psutil.swap_memory()
