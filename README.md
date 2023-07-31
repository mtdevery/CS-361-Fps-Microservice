# CS-361-Fps-Microservice

This Project is a FPS tracking microservice written for use in Python projects. Connect to the FPS tracking server running on your local machine from your project using the FpsClient class and call get_fps once per iteration to update and receive the frames per second of your main program.

Communication Contract:
This project is implemented in Python using the Python built in socket library functionality.
In order to request data from the FPS Microservice send a ping to the port that the FPS Microservice server is running on as demonstrated in the FpsClient class' get_fps function.
In order to receive data from the FPS Microservice utilize the returned value from the FpsClient's get_fps function.
![image](https://github.com/mtdevery/CS-361-Fps-Microservice/assets/107636390/62e883c3-fadd-4d8f-aea0-0301bbf459ff)
