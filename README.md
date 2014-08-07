10188101-网络控制系统设计 课程设计
=====
包含:

1. 数字PID控制算法

  在用户界面下提供简单的系统仿真与其PID控制, PID参数可调,仿真模型可设置,控制延迟可调,给定信号由用户交互完成,仿真结果在图像中显示.
  
2. Socket网络控制

  在用户界面下实现简单的TCP Socket客户端,目标服务器地址和端口可设置，连接后即时显示双方发出的信息，可启用html渲染查看超文本内容.
  
3. 高级控制算法

  在用户界面下提供简单的系统仿真与其基于简单的FNN BP神经网络的控制, 其参数可调,仿真模型可设置,控制延迟可调,训练响应与给定信号由用户交互完成,仿真结果在图像中显示.

---------------
开发平台为Python+Qt4, 仿真通过matplotlib.mplwidget呈现.
高级控制算法采用简单的BP神经网络实现, 通过对原控制对象的响应进行学习训练得到最优的控制系统.

  
10188101-NetworkControlSystem_Works
====
Including:

1. Computer PID controller
  
  A software PID control algorithm in Class CPID, simulation can be demonstrated in GUI plot widget;
  The parameters of PID, delay of controller, target system can be tweaked, the input should be set by user.
  
2. Socket client example

  A simple TCP socket client, with message displayed in text view, host and port can be configured, HTML content can be rendered by Qt.
  
3. Advanced control algorithm

  A simple BP neural network controller is given in this demonstration, simulation can be demonstrated in GUI plot widget;
  The parameters of the neural network, delay of controller, target system can be tweaked, the input should be set by user.
  Check the checkbox to enable controller, or to display the response target system and make neural network learn, press "Train" to train the neural network.

----
It is developed with Python+Qt4, simulation is presented with matplotlib.mplwidget.
