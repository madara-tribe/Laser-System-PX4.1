;; Auto-generated. Do not edit!


(when (boundp 'ros_start::SetVelocity)
  (if (not (find-package "ROS_START"))
    (make-package "ROS_START"))
  (shadow 'SetVelocity (find-package "ROS_START")))
(unless (find-package "ROS_START::SETVELOCITY")
  (make-package "ROS_START::SETVELOCITY"))
(unless (find-package "ROS_START::SETVELOCITYREQUEST")
  (make-package "ROS_START::SETVELOCITYREQUEST"))
(unless (find-package "ROS_START::SETVELOCITYRESPONSE")
  (make-package "ROS_START::SETVELOCITYRESPONSE"))

(in-package "ROS")





(defclass ros_start::SetVelocityRequest
  :super ros::object
  :slots (_x _y ))

(defmethod ros_start::SetVelocityRequest
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:serialization-length
   ()
   (+
    ;; float32 _x
    4
    ;; float32 _y
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _x
       (sys::poke _x (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _y
       (sys::poke _y (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _x
     (setq _x (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _y
     (setq _y (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(defclass ros_start::SetVelocityResponse
  :super ros::object
  :slots (_success ))

(defmethod ros_start::SetVelocityResponse
  (:init
   (&key
    ((:success __success) nil)
    )
   (send-super :init)
   (setq _success __success)
   self)
  (:success
   (&optional (__success :null))
   (if (not (eq __success :null)) (setq _success __success)) _success)
  (:serialization-length
   ()
   (+
    ;; bool _success
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _success
       (if _success (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _success
     (setq _success (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass ros_start::SetVelocity
  :super ros::object
  :slots ())

(setf (get ros_start::SetVelocity :md5sum-) "e99dfd300d1e59a2f817598c6d8f754c")
(setf (get ros_start::SetVelocity :datatype-) "ros_start/SetVelocity")
(setf (get ros_start::SetVelocity :request) ros_start::SetVelocityRequest)
(setf (get ros_start::SetVelocity :response) ros_start::SetVelocityResponse)

(defmethod ros_start::SetVelocityRequest
  (:response () (instance ros_start::SetVelocityResponse :init)))

(setf (get ros_start::SetVelocityRequest :md5sum-) "e99dfd300d1e59a2f817598c6d8f754c")
(setf (get ros_start::SetVelocityRequest :datatype-) "ros_start/SetVelocityRequest")
(setf (get ros_start::SetVelocityRequest :definition-)
      "float32 x
float32 y
---
bool success

")

(setf (get ros_start::SetVelocityResponse :md5sum-) "e99dfd300d1e59a2f817598c6d8f754c")
(setf (get ros_start::SetVelocityResponse :datatype-) "ros_start/SetVelocityResponse")
(setf (get ros_start::SetVelocityResponse :definition-)
      "float32 x
float32 y
---
bool success

")



(provide :ros_start/SetVelocity "e99dfd300d1e59a2f817598c6d8f754c")


