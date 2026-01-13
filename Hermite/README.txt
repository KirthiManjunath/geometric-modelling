Description:
This project contains a simple implementation of hermite curve interpolation that can be used for educational purposes.

Background:
Hermite curves are parametric curves defined by endpoints and end point tangents. Joining successive hermite segments leads to a continuous curve that can be manipulated by changing the end points and tangents of the individual segments.
In this project, I have defined hermite curves to be continuous upto the second derivative. This implies that the user only has to specify the tangents for the first hermite segment.

Instructions:
You can interact with this project in one of 2 ways:
- main_CLI - use this option for precise numerical control
- main_GUI - use this option for a more intuitive, visual exploration of hermite curves 
Run the selected script and respond to the prompts as they appear.

Overview:

Hermite.py
init 
- Initialises tangents and points and stores a reference to the previous hermite segment if applicable. 
- Calls the C2continuity function to auto generate the tangents based on the previous segment
hermite_basis
- Contains the hermite basis functions.
- Returns the hermite curve, smapled along parameter t
C2continuity
- Ensures geometric continuity by initializing the 1st point of the new segment wiht the value of the 2nd point from the previous segment, thus making sure they coincide 
- Ensures C1 continuity by initalizing the 1st tangent of the new segment witht he 2nd tangent of the previous segment
- Ensures C2 continuity by computing the 2nd tangent value

main_CLI.py
Command Line Interface that allows you to specify points and tangents and view the resulting curve.

main_GUI.py
Graphical matplotlib based interface that allows you to add points to the curve by clicking points on the plot



