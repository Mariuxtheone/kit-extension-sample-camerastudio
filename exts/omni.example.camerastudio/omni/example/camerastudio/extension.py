import omni.ext
import omni.ui as ui
import omni.kit.commands
from .csvreader import CSVReader


# Functions and vars are available to other extension as usual in python: `example.python_ext.some_public_function(x)`
def some_public_function(x: int):
    print("[omni.example.camerastudio] some_public_function was called with x: ", x)
    return x ** x


# Any class derived from `omni.ext.IExt` in top level module (defined in `python.modules` of `extension.toml`) will be
# instantiated when extension gets enabled and `on_startup(ext_id)` will be called. Later when extension gets disabled
# on_shutdown() is called.
class CamerastudioExtension(omni.ext.IExt):
    # ext_id is current extension id. It can be used with extension manager to query additional information, like where
    # this extension is located on filesystem.
    def on_startup(self, ext_id):
        print("[omni.example.camerastudio] omni example camerastudio startup")

        self._count = 0
        self.csvreader = CSVReader()

        self._window = ui.Window("Camera Studio", width=300, height=250)
        with self._window.frame:
            with ui.VStack():
                label = ui.Label("Click the button to import a CSV file\nwith the details to generate multiple cameras.")
 
                with ui.HStack():
                    ui.Button("Open File...", clicked_fn=self.csvreader.on_open_file)
                    

                    

    def on_shutdown(self):
        print("[omni.example.camerastudio] omni example camerastudio shutdown")
