# Script Description
This script will use SeleniumAPI and OBS to play an youtube video and record the desktop for 2 minutes.<br><br>
It will create debug logs which will contain the exact time of running the script in their name and exception logs in case they happen.<br><br>
It will also save the recording as a '.mov' file inside the default OBS output directory (usually your Videos folder). You can change that in OBS settings by accesing
File->Settings->Output and inserting your preffered path. This is not mandatory as the script will automatically get the video's path after the recording is over.<br><br>
It will also create a .wav file ( which is the extracted audio from the video recording ) and a nivel_sunet.txt file which will tell you the sound level in dBs.
The repository also includes a file called 'startobs.py' which is just an alternative to 'startobspy.py'. It is not used, but it's functional.<br><br>

- To run the script you have to run main.py.

# System & Python Information
OS : Microsoft Windows 10 pro, V 10.0.19044 Build 19044 <br>
Python : v3.10.5

# Requirements
- Python v3.10.5 + <br>
- OBS v27.2.4 + <br>
- SeleniumAPI <br>
- The following Python packages: numpy pipwin opencv-python pyautogui simpleobsws ffmpeg moviepy scipy soundfile <br>
**NOTE! Some of these libraries will not be used and are only installed because the homework requires them**
- OBS websocket v5.0.0

# How to set-up the environment
- Install Python 3.10.5 <br>
- Set-up the PATH  by adding C:\Program Files\Git\bin and C:\Program Files\Git\cmd\ to your System Environment Variables <br>
- Install PIP by executing 'python get-pip.py' inside Windows Terminal  <br>
- Install SeleniumAPI using 'pip install -U selenium' . Selenium will require a different driver depending on your browser. The drivers can be found here https://selenium-python.readthedocs.io/installation.html#drivers and you can install it them by copying the .exe driver specific to your browser to Python's installation folder or to PATH.<br>
- Install the required packages using 'pip install  numpy pipwin opencv-python pyautogui simpleobsws ffmpeg moviepy scipy soundfile' <br>
- Install pyaudio using 'pipwin pyaudio' or manually <br>
- Install the latest version of OBS from the official site: https://obsproject.com/ <br>
- Install OBS websocket v5.0.0 which you can find here https://github.com/obsproject/obs-websocket <br>
# How to set-up OBS to be compatible with Python Scripts
- Open OBS and select the default settings (1920x1080p, 60fps)<br>
- Select the default scene called "Scene" and create a new source by clicking on the '+'. Here you will select Display Capture and click ok, keeping the default settings for the scene. <br>
- Next, go to File in the left upper corner, select Settings->Output . Here you will modify the Recording format from .mkv to .mov and click apply . <br>
- Go to Tools->Scritps->Python and insert Python's installation folder.
- Finally, go to Tools->web-socket settings and modify the port to 4444 and the password to "secret" so you will not have to change them inside the script when it will connect to the OBS websocket. 
- **!! NOT MANDATORY !!** if you want, you can change the video's output destination to current's project folder path by accesing File->Settings->Output and inserting your custom project path so you can have all the files in one place. 

