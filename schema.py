import arcpy

arcpy.env.workspace = r"C:\Users\Joe.Bullard\OneDrive - Avon Wildlife Trust\Documents\ArcGIS\Projects\ReptileSurvey\ReptileSurvey.gdb"

fc_name = "Reptile_Hibernacula_Locations"
geometry_type = "POINT"

try:
    arcpy.Delete_management(fc_name)
except:
    pass

arcpy.CreateFeatureclass_management(arcpy.env.workspace, fc_name, geometry_type)

fc_fields = [
    {
        "name": "hibernaculum_id", 
        "type": "TEXT",
        "alias": "Hibernaculum ID",
    }, {
        "name": "type",
        "type": "SHORT",
        "alias": "Type",
    }, {
        "name": "hibernaculum_shape",
        "type": "SHORT",
        "alias": "Shape",
    }, {
        "name": "description",
        "type": "TEXT",
        "alias": "Description",
    }
]

for field in fc_fields:
    arcpy.AddField_management(fc_name, field["name"], field["type"], field_alias=field["alias"])
    
arcpy.AddGlobalIDs_management(fc_name)

sr = arcpy.SpatialReference(27700) 
arcpy.DefineProjection_management(fc_name, sr)

insp_table_name = "Hibernaculua_Inspection"

try:
    arcpy.Delete_management(insp_table_name)
except:
    pass

arcpy.management.CreateTable(arcpy.env.workspace, insp_table_name)

table_fields = [
    {
        "name": "date", 
        "type": "DATE",
        "alias": "Date",
    }, {
        "name": "cloud_cover",
        "type": "SHORT",
        "alias": "Cloud cover",
    }, {
        "name": "wind",
        "type": "SHORT",
        "alias": "Wind",
    }, {
        "name": "rainfall",
        "type": "SHORT",
        "alias": "Rainfall",
    }, {
        "name": "external_temp",
        "type": "FLOAT",
        "alias": "External temp",
    }, {
        "name": "internal_temp",
        "type": "FLOAT",
        "alias": "Internal temp",
    }, {
        "name": "internal_humidity",
        "type": "SHORT",
        "alias": "Internal humidity",
    }, {
        "name": "surveyor",
        "type": "TEXT",
        "alias": "Surveyor initials",
    }, {
        "name": "hib_guid",
        "type": "GUID",
        "alias": "Hibernaculum GUID"
        
    }
]

arcpy.AddGlobalIDs_management(insp_table_name)

for field in table_fields:
    arcpy.AddField_management(insp_table_name, field["name"], field["type"], field_alias=field["alias"])

obs_table_name = "Observation"

try:
    arcpy.Delete_management(obs_table_name)
except:
    pass

arcpy.management.CreateTable(arcpy.env.workspace, obs_table_name)

table_fields = [
    {
        "name": "species",
        "type": "SHORT",
        "alias": "Species",
    }, {
        "name": "lifestage",
        "type": "SHORT",
        "alias": "Wind",
    }, {
        "name": "sex",
        "type": "SHORT",
        "alias": "Sex",
    }, {
        "name": "quantity",
        "type": "SHORT",
        "alias": "Quantity",
    }, {
        "name": "note",
        "type": "TEXT",
        "alias": "Note",
    }, {
        "name": "insp_guid",
        "type": "GUID",
        "alias": "Inspection GUID"
        
    }
]

arcpy.AddGlobalIDs_management(obs_table_name)

for field in table_fields:
    arcpy.AddField_management(obs_table_name, field["name"], field["type"], field_alias=field["alias"])

arcpy.CreateRelationshipClass_management(fc_name, insp_table_name, "insp_relation", "SIMPLE",
                                         "Inspection table", "Hibernaculum location",
                                         "NONE", "ONE_TO_MANY", "NONE", "GlobalID", "hib_guid")
arcpy.CreateRelationshipClass_management(insp_table_name, obs_table_name, "obs_relation", "SIMPLE",
                                         "Observation table", "Inspection table",
                                         "NONE", "ONE_TO_MANY", "NONE", "GlobalID", "insp_guid")

domain_dicts = [
    {
        'domain_name': 'hibernaculum_type_domain', 
        'domain_description': 'Codes for hibernaculum type',
        'table': 'Reptile_Hibernacula_Locations',
        'field_name': 'type',
        'coded_values': {
            1: 'Natural',
            2: 'Artificial'
        }
    }, {
        'domain_name': 'hibernaculum_shape_domain', 
        'domain_description': 'Codes for hibernaculum shape',
        'table': 'Reptile_Hibernacula_Locations',
        'field_name': 'hibernaculum_shape',
        'coded_values': {
            1: 'Horseshoe',
            2: 'Round barrow',
            3: 'Long barrow',
            4: 'Other'
        }
    }, {
        'domain_name': 'cloud_cover_domain', 
        'domain_description': 'Codes for cloud cover',
        'table': 'Hibernaculua_Inspection',
        'field_name': 'cloud_cover',
        'coded_values': {
            1: 'Clear',
            2: 'Scatterd cloud',
            3: 'Broken cloud',
            4: 'Overcast'
        }
    }, {
        'domain_name': 'wind_domain', 
        'domain_description': 'Codes for wind speed',
        'table': 'Hibernaculua_Inspection',
        'field_name': 'wind',
        'coded_values': {
            1: 'None',
            2: 'Light',
            3: 'Strong'
        }
    }, {
        'domain_name': 'rainfall_domain', 
        'domain_description': 'Codes for rainfall',
        'table': 'Hibernaculua_Inspection',
        'field_name': 'rainfall',
        'coded_values': {
            1: 'None',
            2: 'Light',
            3: 'Heavy'
        }
    }, {
        'domain_name': 'species_domain', 
        'domain_description': 'Codes for species',
        'table': 'Observation',
        'field_name': 'species',
        'coded_values': {
            1: 'Slow worm',
            2: 'Grass snake',
            3: 'Adder',
            4: 'Common lizard',
            5: 'Unknown',
            6: 'Other - please enter in notes',
        }
    }, {
        'domain_name': 'sex_domain', 
        'domain_description': 'Codes for sex',
        'table': 'Observation',
        'field_name': 'sex',
        'coded_values': {
            1: 'Female',
            2: 'Male',
            3: 'Unknown'
        }
    }, {
        'domain_name': 'lifestage_domain', 
        'domain_description': 'Codes for lifestage',
        'table': 'Observation',
        'field_name': 'lifestage',
        'coded_values': {
            1: 'Juvenille',
            2: 'Sub-adult',
            3: 'Adult'
        }
    },
]

# Define the domain name and description

# Create the domain
for d in domain_dicts:
    arcpy.CreateDomain_management(arcpy.env.workspace, d['domain_name'], d['domain_description'], "SHORT", "CODED")
    
    for code, value in d['coded_values'].items():
        arcpy.AddCodedValueToDomain_management(arcpy.env.workspace, d['domain_name'], code, value)

    arcpy.AssignDomainToField_management(d['table'], d['field_name'], d['domain_name'])
