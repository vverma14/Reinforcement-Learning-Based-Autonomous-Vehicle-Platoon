Requirements for running the CARLA simulator successfully:
Pillow>=3.1.2
numpy>=1.14.5
protobuf>=3.6.0
pygame>=1.9.4
matplotlib>=2.2.2
future>=0.16.0
scipy>=0.17.0
python=3.6
CARLA version=0.9.0

Place the python client folder to the carla simulator folder. 

For running the carla simulator open terminal, navigate to the carla folder and type in the below command:
-CarlaUE4.exe /Game/Maps/RaceTrack -windowed -carla-server -benchmark -fps=30

To run RL agent on Town01/Town02/Racetrack we can use the below code to run it from the carla root folder. Make sure to keep the ports the same. Replace the TownXX with 01 or 02 to run it accordingly.:
CarlaUE4 /Game/Maps/MapName -carla-server -benchmark -fps=10 -windowed -carla-world-port=PORT
RL agent for this can be run using the below command:
python run_RL.py --city-name MapName --port PORT --corl-2017

To run the PID controlled agent on a map, navigate to the Racetrack_PID folder and run the module_7 file using python command. The RL should be run first and then the follower agent shold be run to align the scenarios.

To establish a socket connection run the CLIENT_TESTING.py file from the pythonclient folder right after the RL agent spawns at the desired location. The socket connection the establishes and the code can resume running. If not run the socket connection would wait for a handshake(meaning a response from the listener i.e client) for running and the program would fail.

The program can be terminated anytime with ctrl+C and these commands can be re-run to establish the simulation connection anytime.



