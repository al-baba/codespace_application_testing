import pytest

# from basic_rest_API import our_application_v6

def estimate(kalamata):
  departure = kalamata + 20
  return departure

def test_estimate():
  t_estimate = estimate(15)
  expected = 35
  assert t_estimate == expected


def test_estimate_2():
  t_estimate = estimate(22)
  trip_time = 42
  assert t_estimate == trip_time


def test_estimate_3():
    t_estimate = estimate(10)
    journey_to_dump = 30
    assert t_estimate == journey_to_dump
