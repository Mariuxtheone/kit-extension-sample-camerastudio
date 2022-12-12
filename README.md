# Camera Studio - NVIDIA Omniverse Extension

<img src="https://github.com/Mariuxtheone/kit-extension-sample-camerastudio/blob/main/exts/omni.example.camerastudio/data/icon.png" width="128">

This extension allows to open a CSV file containing information about Camera Settings and generate in-scene Cameras accordingly.

![Image](/exts/omni.example.camerastudio/data/preview.png)

Usage:

The extension generates cameras with the following settings:
-Shot Name
-Focal Length (in mm)
-Horizontal Aperture (in mm)
-Distance from the subject the camera should be placed at the scene (in meters)

1) Create your .csv file with the following header:

```
shot_name,focal_length,aperture,distance
```

e.g.

```
shot_name,focal_length,aperture,distance
establishing_shot,24,2.8,4
wide_shot,14,2.0,4
over_the_shoulder_shot,50,2.8,0.5
point_of_view_shot,85,2.8,0.5
low_angle_shot,24,1.8,0.5
high_angle_shot,100,2.8,1.5
```

2) Open the .csv file via the Extension.
3) The extension will generate the cameras in your scene with the desired shots configured.

# chatGPT Prompt (also works with GPT-3)
This is the prompt that I perfected to generate shots, you might have to run it a few times to get the exact desired results, but this seems to do the trick:

```
list a series of 10 camera shots for an interior video shoot, specifying the focal length of the camera in mm, the horizontal aperture (as number), and the distance the camera should be put at (in meters)

put those settings in a CSV file using this header: shot_name, focal_length, aperture, distance

horizontal aperture should be indicated as number (for example, 2.8) and distance should be indicated as number (for example, for 1 meter, put 1). shot_name has to be represented with underscore format (for example, extreme_close_up_shot)

remove mm and m from the CSV
```


# Extension Project Template

This project was automatically generated.

- `app` - It is a folder link to the location of your *Omniverse Kit* based app.
- `exts` - It is a folder where you can add new extensions. It was automatically added to extension search path. (Extension Manager -> Gear Icon -> Extension Search Path).

Open this folder using Visual Studio Code. It will suggest you to install few extensions that will make python experience better.

Look for "omni.example.camerastudio" extension in extension manager and enable it. Try applying changes to any python files, it will hot-reload and you can observe results immediately.

Alternatively, you can launch your app from console with this folder added to search path and your extension enabled, e.g.:

```
> app\omni.code.bat --ext-folder exts --enable company.hello.world
```

# App Link Setup

If `app` folder link doesn't exist or broken it can be created again. For better developer experience it is recommended to create a folder link named `app` to the *Omniverse Kit* app installed from *Omniverse Launcher*. Convenience script to use is included.

Run:

```
> link_app.bat
```

If successful you should see `app` folder link in the root of this repo.

If multiple Omniverse apps is installed script will select recommended one. Or you can explicitly pass an app:

```
> link_app.bat --app create
```

You can also just pass a path to create link to:

```
> link_app.bat --path "C:/Users/bob/AppData/Local/ov/pkg/create-2021.3.4"
```


# Sharing Your Extensions

This folder is ready to be pushed to any git repository. Once pushed direct link to a git repository can be added to *Omniverse Kit* extension search paths.

Link might look like this: `git://github.com/[user]/[your_repo].git?branch=main&dir=exts`

Notice `exts` is repo subfolder with extensions. More information can be found in "Git URL as Extension Search Paths" section of developers manual.

To add a link to your *Omniverse Kit* based app go into: Extension Manager -> Gear Icon -> Extension Search Path

## Contributing
The source code for this repository is provided as-is and we are not accepting outside contributions.

