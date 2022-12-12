import omni.ext
import omni.ui as ui
import omni.kit.commands
from pxr import UsdGeom
from omni.kit.window.file_importer import get_file_importer
from typing import List, Tuple, Callable, Dict
import csv

from .cameragenerator import CameraGenerator

class CSVReader():

    def __init__(self):
        pass

    def import_handler(self,filename: str, dirname: str, selections: List[str] = []):
                    print(f"> Import '{filename}' from '{dirname}' or selected files '{selections}'")
                    self.openCSV(dirname+filename)

    def on_open_file(self):
        file_importer = get_file_importer()
        file_importer.show_window(
            title="Import File",
            # The callback function called after the user has selected a file.
            import_handler=self.import_handler
            
        )

    #write a function that opens a CSV file, reads the data, and stores it in variables named shot_name, focal_length, aperture, distance
    def openCSV(self,selections):
        with open(selections) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    line_count += 1
                else:
                    shot_name = row[0]
                    print (f'Shot Name: {shot_name}.')
                    focal_length = row[1]
                    print (f'Focal Length: {focal_length}.')
                    aperture = row[2]
                    print (f'Aperture: {aperture}.')
                    distance = row[3]
                    print (f'Distance: {distance}.')

                    #do something with the csv data. in this case, generate a camera
                    cameraGenerator = CameraGenerator()

                    cameraGenerator.generate_camera(str(shot_name), float(focal_length), float(aperture), float(distance))
                    line_count += 1    




