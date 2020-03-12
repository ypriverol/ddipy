from unittest import TestCase

from ddipy.commons import Dataset
from ddipy.dataset_client import DatasetClient


class TestDataset(TestCase):

    def test_get_object_from_json(self):
        client = DatasetClient()
        object_json = client.get_dataset_details("pride", "PXD000210", False)

        dataset = Dataset.get_object_from_json(object_json)
        assert dataset.accession == "PXD000210"
        assert dataset.title == "Proteome analysis by charge state-selective separation of peptides: a multidimensional approach"

        assert len(dataset.dates) > 0
        assert len(dataset.scores) > 0
        assert len(dataset.cross_references) > 0
        assert len(dataset.keywords) > 0
        assert len(dataset.organisms) > 0
        assert len(dataset.get_posttranslational_modifications()) == 7

