# Laser tracking System (Version 4.1)

# abstract
It is automaticallay laser tracking sysytem using AI model. 

Mainly It consist of ：
- yolov7 (object detection)
- Stereo Vision(Depth calurate)
- Hardware PWM component
- 2 servo moter
- handmade laser and so on

This is first prototype as low-end model.
Previous version [PX4.0](https://github.com/madara-tribe/Laser-System-PX4.1/tree/px4.0) 

<b>Parts</b>
```zsh
- Jetson nano
- Adafruit PCA9685 PWM controler
- 2 Serbo motor 
- handmade laser pointer
- CSI camera
```


## version
```zsh
Jetson Nano
JetPack 4.6.0
pytorch 1.10.0
torchvision 0.11
onnx 1.11.0
cpu 
```

# How it work
```zsh

# software calibrate
$ python3 main.py -st

# hard ware calibrate
$ python3 main.py -ht

# take laser tracking system
$ python3 main.py --pwm
```

# Result

<b>YOUTUBE MOVIE LINK</b>

[![PX4.1 X-AXIS](![sddefault](https://github.com/madara-tribe/Laser-System-PX4.1/assets/48679574/1627af82-5892-49d7-b41f-853988a092ca))](https://youtu.be/QchYIQ16owU)
## main improvement point
- Hardware power poverty (jetson nano)
- camera StereoVison accuracy 
- Low-Speed PWM communication
