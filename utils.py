import torch
from torch import nn
import numpy as np


EPSILON = 1e-2

def linear_quantize(samples, q_levels):
    samples = samples.clone()
    samples += 1
    samples /= 2
    samples *= q_levels - EPSILON
    samples += EPSILON / 2
    return samples.long()

def linear_dequantize(samples, q_levels):
    return samples.float() / (q_levels / 2) - 1

def q_zero(q_levels):
    return q_levels // 2
