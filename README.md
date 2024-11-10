Piano_Technique_Analyzer is inspired by the work of Dorothy Taubman and her research into the bio-mechanical motions that enable prodigies and proficient pianists to play well. One of her main discoveries was in forearm rotational motion at the piano; specifically in how forearm rotation allows players to move note to note with speed and ease. There are two types of rotations at the piano: single and double rotation. These rotations are done for every consecutive pair of notes.

When you input piano sheet music (in Music XML format) that is fully notated with fingerings, we will show the following biomechanical information for every pair of fingerings:
1) Which angular direction (right or left) was the hand previously moving in
2) Which rotational movement is necessary to get the hand to the next location (single or double rotation)
3) What is the new angular direction that the hand will be moving in as a result. 

Dependencies: 
pip install music21

How to run:

python getRotations.py - This will run the program on the Chopin excerpt by default

python .\getRotations.py demo_scores\J.S._Bach_Invention_No._4_in_D_Minor.musicxml  - Enter the file path you want to run the program on

NOTE: The program currently only works for right-hand passages and requires that all fingerings be filled in.
 
Output: 

The output will be a text file containing the rotation and directional motion for every pair of notes


