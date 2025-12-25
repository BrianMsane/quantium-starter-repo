from main import app

def test_header_present(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.find_element("h1")
    
    assert header is not None
    assert header.text == "Pink Morsel Sales Visualiser"


def test_visualisation_present(dash_duo):
    dash_duo.start_server(app)
    visualisation = dash_duo.find_element("#sales-line-chart")
    assert visualisation is not None


def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    region_picker = dash_duo.find_element("#region-filter")
    assert region_picker is not None
