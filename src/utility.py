import jsonpickle
import os


def export(obj, path):
    f = open(path, 'w')
    ext = os.path.splitext(path)[1]
    if ext == ".json":
        jsonpickle.set_encoder_options('simplejson', sort_keys=True, indent=0)
        f.write(jsonpickle.encode(obj, unpicklable=False))
    elif ext == ".scad":
        jsonpickle.set_encoder_options('simplejson', sort_keys=True, indent=0)
        f.write(jsonpickle.encode(obj, unpicklable=False))
