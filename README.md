Piano_Technique_Analyzer is inspired by the work of Dorothy Taubman and her research into the bio-mechanical motions that enable prodigies and proficient pianists to play well. One of her main discoveries was in forearm rotational motion at the piano; specifically in how forearm rotation allows players to move note to note with speed and ease. There are two types of rotations at the piano: single and double rotation. These rotations are done for every consecutive pair of notes.

This program takes a musicXML file that has fingering fully notated for every note and outputs a text file that classifies every rotation while also showing how the angular direction of the hand shifts because of the new note being played.

Dependencies: 
pip install music21

How to run:

python getRotations.py - This will run the program on the Chopin excerpt by default

python .\getRotations.py demo_scores\J.S._Bach_Invention_No._4_in_D_Minor.musicxml  - Enter the file path you want to run the program on

NOTE: The program currently only works for right-hand passages and requires that all fingerings be filled in.
 
Output: 

The output will be a text file containing the rotation and directional motion for every pair of notes


