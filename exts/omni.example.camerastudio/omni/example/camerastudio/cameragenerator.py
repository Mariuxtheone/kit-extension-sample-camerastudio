import omni.ext
import omni.ui as ui
import omni.kit.commands
from pxr import UsdGeom
from omni.kit.window.file_importer import get_file_importer

class CameraGenerator():
    def __init__(self):
        pass

    def generate_camera(self, shot_name, focal_length, aperture, distance):
                    #generate camera
                    omni.kit.commands.execute("CreatePrimWithDefaultXform",
                    prim_type="Camera",
                    prim_path="/World/"+shot_name,
                    attributes={
                        "projection": UsdGeom.Tokens.perspective,
                        "focalLength": focal_length,
                        "horizontalAperture": aperture,
                        
                    }
                    )
                
                    #move camera
                    omni.kit.commands.execute('TransformMultiPrimsSRTCpp',
                        count=1,
                        paths=['/World/'+shot_name],
                        new_translations=[0, 0, distance*1000],
                        new_rotation_eulers=[-0.0, -0.0, -0.0],
                        new_rotation_orders=[1, 0, 2],
                        new_scales=[1.0, 1.0, 1.0],
                        old_translations=[0.0, 0.0, 0.0],
                        old_rotation_eulers=[0.0, -0.0, -0.0],
                        old_rotation_orders=[1, 0, 2],
                        old_scales=[1.0, 1.0, 1.0],
                        usd_context_name='',
                        time_code=0.0)

