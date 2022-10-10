from dataclasses import is_dataclass
import unittest
from src.__seedwork.domain.entities import Entity


class TestEntityUnit(unittest.TestCase):
  
  def test_if_is_a_dataclass(self):
    self.assertTrue(is_dataclass(Entity))