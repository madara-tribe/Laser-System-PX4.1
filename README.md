# Laser tracking System with object detection  (Prototype)

# abstract
It is automaticallay laser tracking sysytem using AI model. 

Mainly It consist of ：
・　yolov7 (object detection)
：Stereo Vision(Depth calurate)
：Hardware PWM component
・2 servo moter
・handmade laser and so on

This is first prototype as low-end model.
Previous version Px4.0 

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


## main improvement point
・Hardware power poverty (jetson nano)
・camera StereoVison accuracy 
・Low-Speed PWM communication
