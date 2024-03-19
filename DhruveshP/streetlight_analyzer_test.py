import streetlight_analyzer

streetlight_analyzer.streetlight_fc = "path/to/street_light_feature_class"
streetlight_analyzer.roads_cl_fc = "path/to/roads_center_lines_feature_class"
streetlight_analyzer.road_name_field = "ROAD_NAME_"
def test_get_streetlight_count():
   
    expected_count = 39
    actual_count = streetlight_analyzer.get_streetlight_count("CARLING", 0.0002)
    assert expected_count == actual_count


