# Camera Studio

This extension allows to open a CSV file containing information about Camera Settings and generate in-scene Cameras accordingly.

Usage:

The extension generates cameras with the following settings:
-Shot Name
-Focal Length (in mm)
-Horizontal Aperture (in mm)
-Distance from the subject the camera should be placed at the scene (in meters)

1) Create your .csv file with the following header:

shot_name,focal_length,aperture,distance

e.g.

shot_name,focal_length,aperture,distance
establishing_shot,24,2.8,4
wide_shot,14,2.0,4
over_the_shoulder_shot,50,2.8,0.5
point_of_view_shot,85,2.8,0.5
low_angle_shot,24,1.8,0.5
high_angle_shot,100,2.8,1.5

2) Open the .csv file via the Extension.
3) The extension will generate the cameras in your scene with the desired shots configured.
