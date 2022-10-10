from dataclasses import is_dataclass
import unittest

from src.__seedwork.domain.exceptions import InvalidUuidException
from src.__seedwork.domain.value_objects import UniqueEntityId

class TestUniqueEntityId(unittest.TestCase):
  def test_if_is_a_dataclass(self):
    self.assertTrue(is_dataclass(UniqueEntityId))
    
  def test_throw_an_exception_when_uuid_is_invalid(self):
    with self.assertRaises(InvalidUuidException) as assert_error:
      UniqueEntityId('fake id')
    self.assertEqual(assert_error.exception.args[0], 'ID must be a valid UUID')