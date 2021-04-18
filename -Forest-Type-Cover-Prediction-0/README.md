The problem statement revolves around the need to predict the forest cover type (the predominant kind of tree cover) from strictly cartographic variables (as opposed to remotely sensed data).

It includes four wilderness areas located in the Roosevelt National Forest of northern Colorado. These areas represent forests with minimal human-caused disturbances, so that existing forest cover types are more a result of ecological processes rather than forest management practices.

The study area includes four wilderness areas located in the Roosevelt National Forest of northern Colorado. Each observation is a 30m x 30m patch. You are asked to predict an integer classification for the forest cover type. The seven types are:

1 - Spruce/Fir 2 - Lodgepole Pine 3 - Ponderosa Pine 4 - Cottonwood/Willow 5 - Aspen 6 - Douglas-fir 7 - Krummholz

About the Dataset:
The snapshot of the data, you will be working on :

forest_data

You can observe there are more than 20+ features in the dataset. We will be working with this dataset to gather insights and look at the feature importance of each feature contributing towards the target variable. The data is in raw form (not scaled) and contains binary columns of data for qualitative independent variables such as wilderness areas and soil type.

Why solve this project?
After completing this project, you will have a better understanding of how feature selection affects the performance of a machine learning model. In this project, you will apply the following concepts.

How are the features important to our model.
How to select the most significant features out of many.
How to perform univariate feature selection.
How to perform a multivariate feature selection.
The data set (15120 observations) contains both features and the Cover_Type.

Feature	Description
Elevation	Elevation in meters
Aspect	Aspect in degrees azimuth
Slope	Slope in degrees
Horizontal Distance To Hydrology	Horz Dist to nearest surface water features
Vertical Distance To Hydrology	Vert Dist to nearest surface water features
Horizontal Distance To Roadways	Horz Dist to nearest roadway
Hillshade_9am (0 to 255 index)	Hillshade index at 9am, summer solstice
Hillshade_Noon (0 to 255 index)	Hillshade index at noon, summer solstice
Hillshade_3pm (0 to 255 index)	Hillshade index at 3pm, summer solstice
Horizontal Distance To Fire Points	Horizontal Dist to nearest wildfire ignition points
Wilderness_Area (4 binary columns, 0 = absence or 1 = presence)	Wilderness area designation
Soil_Type (40 binary columns, 0 = absence or 1 = presence)	Soil Type designation
Cover_Type (7 types, integers 1 to 7)	Forest Cover Type designation
The wilderness areas are:

Rawah Wilderness Area
Neota Wilderness Area
Comanche Peak Wilderness Area
Cache la Poudre Wilderness Area
The soil types are:

Cathedral family - Rock outcrop complex, extremely stony.
Vanet - Ratake families complex, very stony.
Haploborolis - Rock outcrop complex, rubbly.
Ratake family - Rock outcrop complex, rubbly.
Vanet family - Rock outcrop complex, rubbly.
Vanet - Wetmore families - Rock outcrop complex, stony.
Gothic family.
Supervisor - Limber families complex.
Troutville family, very stony.
Bullwark - Catamount families - Rock outcrop complex, rubbly.
Bullwark - Catamount families - Rock land complex, rubbly.
Legault family - Rock land complex, stony.
Catamount family - Rock land - Bullwark family complex, rubbly.
Pachic Argiborolis - Aquolis complex.
unspecified in the USFS Soil and ELU Survey.
Cryaquolis - Cryoborolis complex.
Gateview family - Cryaquolis complex.
Rogert family, very stony.
Typic Cryaquolis - Borohemists complex.
Typic Cryaquepts - Typic Cryaquolls complex.
Typic Cryaquolls - Leighcan family, till substratum complex.
Leighcan family, till substratum, extremely bouldery.
Leighcan family, till substratum - Typic Cryaquolls complex.
Leighcan family, extremely stony.
Leighcan family, warm, extremely stony.
Granile - Catamount families complex, very stony.
Leighcan family, warm - Rock outcrop complex, extremely stony.
Leighcan family - Rock outcrop complex, extremely stony.
Como - Legault families complex, extremely stony.
Como family - Rock land - Legault family complex, extremely stony.
Leighcan - Catamount families complex, extremely stony.
Catamount family - Rock outcrop - Leighcan family complex, extremely stony.
Leighcan - Catamount families - Rock outcrop complex, extremely stony.
Cryorthents - Rock land complex, extremely stony.
Cryumbrepts - Rock outcrop - Cryaquepts complex.
Bross family - Rock land - Cryumbrepts complex, extremely stony.
Rock outcrop - Cryumbrepts - Cryorthents complex, extremely stony.
Leighcan - Moran families - Cryaquolls complex, extremely stony.
Moran family - Cryorthents - Leighcan family complex, extremely stony.
Moran family - Cryorthents - Rock land complex, extremely stony.
