import streetlight_analyzer

streetlight_analyzer.streetlight_fc = "E:\acgis\gis4207_prog\Data\Ottawa\Street_Lights"
streetlight_analyzer.roads_cl_fc = "E:\acgis\gis4207_prog\Data\Ottawa\Road_Centrelines"
streetlight_analyzer.road_name_field = "ROAD_NAME_"
def test_get_streetlight_count():
   
    expected_count = 39
    actual_count = streetlight_analyzer.get_streetlight_count("CARLING", 0.0002)
    assert expected_count == actual_count


