# Laser tracking System with object detection  (Prototype)

# abstract
It has Minimum functionality for tracking laser sysytem. This is first prototype as low-end model.

Its system include object detection(yolov7), PWM control, 2 servo moter, handmade laser and so on.

<b>Parts</b>
- Jetson nano
- Adafruit PCA9685 PWM controler
- 2 Serbo motor 
- handmade laser pointer
- CSI camera


## version
```zsh
Jetson Nano
JetPack 4.6.0
pytorch 1.10.0
torchvision 0.11
onnx 1.11.0
cpu 
```


## overall
<img src="https://user-images.githubusercontent.com/48679574/217874634-fa31091c-6249-4292-a78b-f9941e1fd80e.png" width="500" height="350"/>


# How it work

## hardware (laser itself)

<img src="https://user-images.githubusercontent.com/48679574/217854214-5da2563d-dd53-4ec9-9cc8-04690d55e8de.gif" width="300" height="500"/>

## Software (laser controller)

<img src="https://user-images.githubusercontent.com/48679574/217854150-becb5933-0887-425e-b090-2a8402d5c0c4.gif" width="500" height="400"/>

# References
・[Laser_control](https://github.com/Ildaron/Laser_control)
