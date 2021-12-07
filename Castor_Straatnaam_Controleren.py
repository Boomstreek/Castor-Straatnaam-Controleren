# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Straatnaam_Controleren.py
# Created on: 2021-12-07 15:22:30.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Set the necessary product code
# import arcinfo


# Import arcpy module
import arcpy


# Local variables:
Opdelend = "Opdelend"
Wegdeel = Opdelend
Gebiedsindeling__wegaslijnen_ = "Gebiedsindeling (wegaslijnen)"
Wegaslijnen = Gebiedsindeling__wegaslijnen_
Wegaslijn_2 = "in_memory\\Wegaslijn_2"
Wegaslijn_2_GeneratePoints_10m = "in_memory\\Wegaslijn_2_GeneratePoints_10m"
Distance__value_or_field_ = "5 Meters"
Wegaslijn_2_GeneratePoints_1 = "in_memory\\Wegaslijn_2_GeneratePoints_1"
Wegaslijn_2_Erase = "in_memory\\Wegaslijn_2_Erase"
Wegaslijn_2_Erase__2_ = Wegaslijn_2_Erase
Wegaslijn_2_Erase_Generate5meter = "in_memory\\Wegaslijn_2_Erase_Generate5meter"
Wegaslijn_2_Points_ThiessenPolygon = "in_memory\\Wegaslijn_2_Points_ThiessenPolygon"
Wegaslijn_Buffer_10meter_Dissolved = "in_memory\\Wegaslijn_Buffer_10meter_Dissolved"
Wegdeel_SpatialJoin = "in_memory\\Wegdeel_SpatialJoin"

# Process: Select Data (2)
arcpy.SelectData_management(Opdelend, "Wegdeel")

# Process: Select Data
arcpy.SelectData_management(Gebiedsindeling__wegaslijnen_, "Wegaslijnen")

# Process: Copy Features (2)
arcpy.CopyFeatures_management(Wegaslijnen, Wegaslijn_2, "", "0", "0", "0")

# Process: Generate Points Along Lines
arcpy.GeneratePointsAlongLines_management(Wegaslijn_2, Wegaslijn_2_GeneratePoints_10m, "PERCENTAGE", "", "100", "END_POINTS")

# Process: Buffer (2)
arcpy.Buffer_analysis(Wegaslijn_2_GeneratePoints_10m, Wegaslijn_2_GeneratePoints_1, Distance__value_or_field_, "FULL", "ROUND", "NONE", "", "PLANAR")

# Process: Erase
arcpy.Erase_analysis(Wegaslijn_2, Wegaslijn_2_GeneratePoints_1, Wegaslijn_2_Erase, "")

# Process: Densify
arcpy.Densify_edit(Wegaslijn_2_Erase, "DISTANCE", "4 Meters", "0,1 Meters", "10")

# Process: Generate Points Along Lines (2)
arcpy.GeneratePointsAlongLines_management(Wegaslijn_2_Erase__2_, Wegaslijn_2_Erase_Generate5meter, "DISTANCE", "5 Meters", "", "END_POINTS")

# Process: Create Thiessen Polygons
arcpy.CreateThiessenPolygons_analysis(Wegaslijn_2_Erase_Generate5meter, Wegaslijn_2_Points_ThiessenPolygon, "ALL")

# Process: Dissolve
arcpy.Dissolve_management(Wegaslijn_2_Points_ThiessenPolygon, Wegaslijn_Buffer_10meter_Dissolved, "STT_NAAM;MSLINK;WVK_ID", "", "MULTI_PART", "DISSOLVE_LINES")

# Process: Spatial Join
arcpy.SpatialJoin_analysis(Wegdeel, Wegaslijn_Buffer_10meter_Dissolved, Wegdeel_SpatialJoin, "JOIN_ONE_TO_ONE", "KEEP_ALL", "", "HAVE_THEIR_CENTER_IN", "", "")

