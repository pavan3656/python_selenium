import pytest


@pytest.mark.usefixtures("dataload")
class Testexample2:

    def test_editprofile(self, dataload):
        print(dataload)