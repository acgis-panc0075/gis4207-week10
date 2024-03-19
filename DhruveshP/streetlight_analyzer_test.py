import streetlight_analyzer

streetlight_analyzer.streetlight_fc = "E:\acgis\gis4207_prog\Data\Ottawa\Street_Lights"
streetlight_analyzer.roads_cl_fc = "E:\acgis\gis4207_prog\Data\Ottawa\Road_Centrelines"
streetlight_analyzer.road_name_field = "ROAD_NAME_"
def test_get_streetlight_count():
   
    expected_count = 39
    actual_count = streetlight_analyzer.get_streetlight_count("CARLING", 0.0002)
    assert expected_count == actual_count

def test_get_unique_values():
    expected_values = {"Road1", "Road2", "Road3"}  
    actual_values = streetlight_analyzer._get_unique_values("E:\acgis\gis4207_prog\Data\Ottawa\Road_Centrelines", "FIELD_NAME")  
    assert expected_values == actual_values

def test_save_streetlights():
    streetlight_analyzer.save_streetlights("CARLING", 0.0002, "output_streetlights_fc")

def test_show_road_names():
    streetlight_analyzer.show_road_names()
  


