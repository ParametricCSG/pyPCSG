import jsonpickle
import os

def export(obj, path):
	file = open(path, 'w')
	ext = os.path.splitext(path)[1]
	if ext == ".json":
		jsonpickle.set_encoder_options('simplejson', sort_keys=True, indent = 0)
		file.write(jsonpickle.encode(obj, unpicklable=False))

