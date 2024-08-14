import pytest

from our_app import our_application_v6

def estimate(kalamata):
  departure = kalamata + 20
  return departure 

def test_estimate():
  t_estimate = estimate(15)
  expected = 35
  assert t_estimate == expected 
