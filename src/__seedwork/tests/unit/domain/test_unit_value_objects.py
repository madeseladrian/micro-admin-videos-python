from dataclasses import is_dataclass
import unittest

from src.__seedwork.domain.value_objects import UniqueEntityId


class TestUniqueEntityId(unittest.TestCase):
  def test_if_is_a_dataclass(self):
    self.assertTrue(is_dataclass(UniqueEntityId))