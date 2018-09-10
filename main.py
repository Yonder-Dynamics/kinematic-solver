#!/usr/bin/env python3

import json

import numpy

import redis

from ikpy.chain import Chain
from ikpy.link import URDFLink


# Orientation Convention
# x: forward
# y: left
# z: up


def build_link(name, length):
    return URDFLink(
        name=name,
        translation_vector=(length, 0, 0),
        orientation=(0, 0, 0),
        rotation=(0, 0, 1),
    )


def build_chain(names_and_lengths):
    return Chain(links=[
        build_link(name, length)
        for name, length in names_and_lengths
    ])


def translation_matrix(x, y, z):
    return numpy.matrix([
        [1, 0, 0, x],
        [0, 1, 0, y],
        [0, 0, 1, z],
        [0, 0, 0, 1],
    ])


def solve_position(chain, target):
    return arm_chain.inverse_kinematics(
        target=translation_matrix(*target),
        initial_position=(0, 0, 0),
    )


def unpack_response(response):
    return response.decode('utf-8', 'strict')


def unpack_target(response):
    target = json.loads(unpack_response(response))
    return (target['x'], target['y'], target['z'])


if __name__ == "__main__":
    arm_chain = build_chain([
        ("humerus", 1),
        ("ulna", 1),
        ("carpal", 1),
    ])

    print("got here")
    r = redis.StrictRedis(host='rover-core', port='6379')
    while True:
        target = unpack_target(r.brpop("arm:targets")[1])
        sol = solve_position(arm_chain, target)
        print(sol)
