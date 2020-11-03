import pickle
from transform_data import *
import os

def serialize(path, coeffs, time, name, family, order):
    to_serialize = TransformData(coeffs, time, name, family, order)
    path = os.path.join(path, name + ".fal")
    with open(path, 'wb') as output:
        pickle.dump(to_serialize, output)

def deserialize(path, name):
    name, file_extension = os.path.splitext(name)
    path = os.path.join(path, name + ".fal")
    with open(path, 'rb') as input:
        transform = pickle.load(input)
        return (transform.coeffs, transform.time, transform.name, transform.family, transform.order)
