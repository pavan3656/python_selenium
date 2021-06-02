import pytest

@pytest.fixture()
def dataload():

    print("user profile data is begin created")
    return["rahul","pavan","pavanraghu97.com"]


@pytest.fixture(params=[("chrome", "pavan", "shell"), ("varin", "kumar"), "IE" ])
def crossBrowser(request):
    return request.param