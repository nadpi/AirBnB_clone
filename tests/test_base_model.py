#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel  # Adjust the import according to your project structure

class TestBaseModel(unittest.TestCase):
    '''tests for BaseModel'''

    def testSave(self):
        my_model = BaseModel()
        my_model_updated = my_model.updated_at
        my_model.save()
        my_model_updated2 = my_model.updated_at
        self.assertNotEqual(my_model_updated, my_model_updated2, "updated_at should be different after save")

    def test2IDS(self):
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id, "ids should differ")
    def testStr(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        expected_str = my_model.__str__()
        self.assertEqual(str(my_model), expected_str, "The __str__ method output is incorrect")

    def testUpdatedAt(self):
        my_model = BaseModel()
        self.assertIsNotNone(my_model.updated_at, "updated_at should be initialized")
        self.assertIsInstance(my_model.updated_at, datetime, "updated_at should be a datetime object")

    def testTo_dict(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        self.assertIsInstance(my_model_json, dict, "to_dict should return a dictionary")
        self.assertIn('id', my_model_json, "to_dict should include id")
        self.assertIn('created_at', my_model_json, "to_dict should include created_at")
        self.assertIn('updated_at', my_model_json, "to_dict should include updated_at")
        self.assertEqual(my_model_json['name'], "My First Model", "to_dict should include name attribute")
        self.assertEqual(my_model_json['my_number'], 89, "to_dict should include my_number attribute")

    def testID(self):
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id, "id should be initialized")
        self.assertIsInstance(my_model.id, str, "id should be a string")

    def testCreatedAt(self):
        my_model = BaseModel()
        self.assertIsNotNone(my_model.created_at, "created_at should be initialized")
        self.assertIsInstance(my_model.created_at, datetime, "created_at should be a datetime object")

if __name__ == "__main__":
    unittest.main()

