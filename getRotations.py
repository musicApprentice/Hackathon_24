from music21 import converter, note
import sys
import warnings
warnings.filterwarnings("ignore")

def get_fingering_from_file(file_path):
    score = converter.parse(file_path)

    fingering_array = []
    for part in score.parts:
        for element in part.flatten().notes:
            if isinstance(element, note.Note):
                for articulation in element.articulations:
                    fingering_string = str(articulation)
                    if "Fingering" in fingering_string:
                        fingering_array.append(fingering_string[-2])
    return fingering_array

def get_rotations(fingering_array):
    rotation_array = []
    for i in range(len(fingering_array)-1):
        if i ==0:
            previousDirection = "None"
            currentFinger = "None"
            nextFinger = fingering_array[i]
            
            rotation = get_rotation_and_direction_from_chart(previousDirection, currentFinger, nextFinger)
            rotation_array.append(rotation)
        
        else:
            
            previousDirection = rotation_array[i-1]["resulting_direction"]
            currentFinger = fingering_array[i-1]
            nextFinger = fingering_array[i]
            
            
            rotation = get_rotation_and_direction_from_chart(previousDirection, currentFinger, nextFinger)
            rotation_array.append(rotation)
    return rotation_array

rotation_chart = [
# Starting conditions, this is an oversimplification because the way you initiate has to do with what finger you plan to follow up with (edge case)
    
    {"current_direction": "None", "current_finger": "None", "next_finger": "1", "resulting_direction": "Left", "rotation": "Double"},
    {"current_direction": "None", "current_finger": "None", "next_finger": "2", "resulting_direction": "Left", "rotation": "Double"},
    {"current_direction": "None", "current_finger": "None", "next_finger": "3", "resulting_direction": "Left", "rotation": "Double"},
    {"current_direction": "None", "current_finger": "None", "next_finger": "4", "resulting_direction": "Left", "rotation": "Double"},
    {"current_direction": "None", "current_finger": "None", "next_finger": "5", "resulting_direction": "Right", "rotation": "Double"},

    
    
    {"current_direction": "Right", "current_finger": "5", "next_finger": "1", "resulting_direction": "Left", "rotation": "Single"},
    {"current_direction": "Right", "current_finger": "5", "next_finger": "2", "resulting_direction": "Left", "rotation": "Single"},
    {"current_direction": "Right", "current_finger": "5", "next_finger": "3", "resulting_direction": "Left", "rotation": "Single"},
    {"current_direction": "Right", "current_finger": "5", "next_finger": "4", "resulting_direction": "Left", "rotation": "Single"},

    {"current_direction": "Left", "current_finger": "1", "next_finger": "2", "resulting_direction": "Right", "rotation": "Single"},
    {"current_direction": "Left", "current_finger": "1", "next_finger": "3", "resulting_direction": "Right", "rotation": "Single"},
    {"current_direction": "Left", "current_finger": "1", "next_finger": "4", "resulting_direction": "Right", "rotation": "Single"},
    {"current_direction": "Left", "current_finger": "1", "next_finger": "5", "resulting_direction": "Right", "rotation": "Single"},

    {"current_direction": "Left", "current_finger": "2", "next_finger": "1", "resulting_direction": "Left", "rotation": "Double"},
    {"current_direction": "Left", "current_finger": "2", "next_finger": "3", "resulting_direction": "Right", "rotation": "Single"},
    {"current_direction": "Left", "current_finger": "2", "next_finger": "4", "resulting_direction": "Right", "rotation": "Single"},
    {"current_direction": "Left", "current_finger": "2", "next_finger": "5", "resulting_direction": "Right", "rotation": "Single"},

    {"current_direction": "Right", "current_finger": "2", "next_finger": "1", "resulting_direction": "Left", "rotation": "Single"},
    {"current_direction": "Right", "current_finger": "2", "next_finger": "3", "resulting_direction": "Right", "rotation": "Double"},
    {"current_direction": "Right", "current_finger": "2", "next_finger": "4", "resulting_direction": "Right", "rotation": "Double"},
    {"current_direction": "Right", "current_finger": "2", "next_finger": "5", "resulting_direction": "Right", "rotation": "Double"},

    {"current_direction": "Right", "current_finger": "2", "next_finger": "1", "resulting_direction": "Left", "rotation": "Single"},
    {"current_direction": "Right", "current_finger": "2", "next_finger": "3", "resulting_direction": "Right", "rotation": "Double"},
    {"current_direction": "Right", "current_finger": "2", "next_finger": "4", "resulting_direction": "Right", "rotation": "Double"},
    {"current_direction": "Right", "current_finger": "2", "next_finger": "5", "resulting_direction": "Right", "rotation": "Double"},

    {"current_direction": "Left", "current_finger": "2", "next_finger": "1", "resulting_direction": "Left", "rotation": "Double"},
    {"current_direction": "Left", "current_finger": "2", "next_finger": "3", "resulting_direction": "Right", "rotation": "Single"},
    {"current_direction": "Left", "current_finger": "2", "next_finger": "4", "resulting_direction": "Right", "rotation": "Single"},
    {"current_direction": "Left", "current_finger": "2", "next_finger": "5", "resulting_direction": "Right", "rotation": "Single"},

    {"current_direction": "Right", "current_finger": "2", "next_finger": "1", "resulting_direction": "Left", "rotation": "Single"},
    {"current_direction": "Right", "current_finger": "2", "next_finger": "3", "resulting_direction": "Right", "rotation": "Double"},
    {"current_direction": "Right", "current_finger": "2", "next_finger": "4", "resulting_direction": "Right", "rotation": "Double"},
    {"current_direction": "Right", "current_finger": "2", "next_finger": "5", "resulting_direction": "Right", "rotation": "Double"},

    {"current_direction": "Right", "current_finger": "3", "next_finger": "1", "resulting_direction": "Left", "rotation": "Single"},
    {"current_direction": "Right", "current_finger": "3", "next_finger": "2", "resulting_direction": "Left", "rotation": "Single"},
    {"current_direction": "Right", "current_finger": "3", "next_finger": "4", "resulting_direction": "Right", "rotation": "Double"},
    {"current_direction": "Right", "current_finger": "3", "next_finger": "5", "resulting_direction": "Right", "rotation": "Double"},

    {"current_direction": "Left", "current_finger": "3", "next_finger": "1", "resulting_direction": "Left", "rotation": "Double"},
    {"current_direction": "Left", "current_finger": "3", "next_finger": "2", "resulting_direction": "Left", "rotation": "Double"},
    {"current_direction": "Left", "current_finger": "3", "next_finger": "4", "resulting_direction": "Right", "rotation": "Single"},
    {"current_direction": "Left", "current_finger": "3", "next_finger": "5", "resulting_direction": "Right", "rotation": "Single"},

    {"current_direction": "Left", "current_finger": "4", "next_finger": "1", "resulting_direction": "Left", "rotation": "Double"},
    {"current_direction": "Left", "current_finger": "4", "next_finger": "2", "resulting_direction": "Left", "rotation": "Double"},
    {"current_direction": "Left", "current_finger": "4", "next_finger": "3", "resulting_direction": "Right", "rotation": "Double"},
    {"current_direction": "Left", "current_finger": "4", "next_finger": "5", "resulting_direction": "Right", "rotation": "Single"},

    {"current_direction": "Right", "current_finger": "4", "next_finger": "1", "resulting_direction": "Left", "rotation": "Single"},
    {"current_direction": "Right", "current_finger": "4", "next_finger": "2", "resulting_direction": "Left", "rotation": "Single"},
    {"current_direction": "Right", "current_finger": "4", "next_finger": "3", "resulting_direction": "Left", "rotation": "Single"},
    {"current_direction": "Right", "current_finger": "4", "next_finger": "5", "resulting_direction": "Right", "rotation": "Double"}

    
]
            
def get_rotation_and_direction_from_chart(previousDirection, currentFinger, nextFinger):
    for entry in rotation_chart:
        if (entry["current_direction"] == previousDirection and 
            entry["current_finger"] == currentFinger and
            entry["next_finger"] == nextFinger):
            return entry
                  
def write_array_to_file(array, fileName):
    with open("Motions.txt", 'w') as file:
        file.write(f"{fileName}\n")
        for element in array:
            file.write(f"{element}\n")  
    print("Processing finished")
    print("Please check your Motions.txt file for output")      
      

def main():
    file = "File"
    if len(sys.argv) > 1:
        file = sys.argv[1]
    else:
        file = "demo_scores\Chopin_Nocturne_Op9_No2_Excerpt.musicxml"

    fingerings = get_fingering_from_file(file)
    solutionArray = (get_rotations(fingerings))
    write_array_to_file(solutionArray, file)
if __name__ == "__main__":
    main()               
              
                                
                    
        