// Generated by gencpp from file ros_start/SetVelocity.msg
// DO NOT EDIT!


#ifndef ROS_START_MESSAGE_SETVELOCITY_H
#define ROS_START_MESSAGE_SETVELOCITY_H

#include <ros/service_traits.h>


#include <ros_start/SetVelocityRequest.h>
#include <ros_start/SetVelocityResponse.h>


namespace ros_start
{

struct SetVelocity
{

typedef SetVelocityRequest Request;
typedef SetVelocityResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct SetVelocity
} // namespace ros_start


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::ros_start::SetVelocity > {
  static const char* value()
  {
    return "e99dfd300d1e59a2f817598c6d8f754c";
  }

  static const char* value(const ::ros_start::SetVelocity&) { return value(); }
};

template<>
struct DataType< ::ros_start::SetVelocity > {
  static const char* value()
  {
    return "ros_start/SetVelocity";
  }

  static const char* value(const ::ros_start::SetVelocity&) { return value(); }
};


// service_traits::MD5Sum< ::ros_start::SetVelocityRequest> should match
// service_traits::MD5Sum< ::ros_start::SetVelocity >
template<>
struct MD5Sum< ::ros_start::SetVelocityRequest>
{
  static const char* value()
  {
    return MD5Sum< ::ros_start::SetVelocity >::value();
  }
  static const char* value(const ::ros_start::SetVelocityRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::ros_start::SetVelocityRequest> should match
// service_traits::DataType< ::ros_start::SetVelocity >
template<>
struct DataType< ::ros_start::SetVelocityRequest>
{
  static const char* value()
  {
    return DataType< ::ros_start::SetVelocity >::value();
  }
  static const char* value(const ::ros_start::SetVelocityRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::ros_start::SetVelocityResponse> should match
// service_traits::MD5Sum< ::ros_start::SetVelocity >
template<>
struct MD5Sum< ::ros_start::SetVelocityResponse>
{
  static const char* value()
  {
    return MD5Sum< ::ros_start::SetVelocity >::value();
  }
  static const char* value(const ::ros_start::SetVelocityResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::ros_start::SetVelocityResponse> should match
// service_traits::DataType< ::ros_start::SetVelocity >
template<>
struct DataType< ::ros_start::SetVelocityResponse>
{
  static const char* value()
  {
    return DataType< ::ros_start::SetVelocity >::value();
  }
  static const char* value(const ::ros_start::SetVelocityResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // ROS_START_MESSAGE_SETVELOCITY_H
