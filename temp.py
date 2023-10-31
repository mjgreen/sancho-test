import random
mytasks = ["control", "reward", "valence"]
random.shuffle(mytasks)
the_current_task = mytasks[0]
this_task_msg = "Task is: " + the_current_task

if the_current_task == "control":

    possible_labels=['air', 'earth', 'sky']
    random.shuffle(possible_labels)
    Label1_type = possible_labels[0]
    Label1_type_msg = "Label 1 is: " + Label1_type
    Label2_type = possible_labels[1]
    Label2_type_msg = "Label 2 is: " + Label2_type    
    Label3_type = possible_labels[2]
    Label3_type_msg = "Label 3 is: " + Label3_type

    indices=[0,1,2]
    random.shuffle(indices)
    possible_file_names =  ['T.bmp', 'S.bmp', 'C.bmp']
    possible_shape_names = ['Triangle',     'Square',     'Circle']

    Shape1_shape_name = possible_shape_names[indices[0]] 
    Shape1_file_name  = possible_file_names[indices[0]] 
    Shape1_msg = "Shape 1 is: " + Shape1_shape_name
    Shape2_shape_name = possible_shape_names[indices[1]]
    Shape2_file_name  = possible_file_names[indices[1]]
    Shape2_msg = "Shape 2 is: " + Shape2_shape_name
    Shape3_shape_name = possible_shape_names[indices[2]]
    Shape3_file_name  = possible_file_names[indices[2]]
    Shape3_msg = "Shape 3 is: " + Shape3_shape_name

elif the_current_task == "reward":
    # then 
    possible_labels=['£100', '£50', '£0']
    random.shuffle(possible_labels)
    Label1_type = possible_labels[0]
    
    Label1_type_msg = "Label 1 is: " + Label1_type
    Label2_type = possible_labels[1]
    Label2_type_msg = "Label 2 is: " + Label2_type    
    Label3_type = possible_labels[2]
    Label3_type_msg = "Label 3 is: " + Label3_type

    indices=[0,1,2]
    random.shuffle(indices)
    possible_file_names =  ['P.bmp', 'D.bmp', 'O.bmp']
    possible_shape_names = ['Pentagon',     'Diamond',     'Oval']

    Shape1_shape_name = possible_shape_names[indices[0]] 
    Shape1_file_name  = possible_file_names[indices[0]] 
    Shape1_msg = "Shape 1 is: " + Shape1_shape_name
    Shape2_shape_name = possible_shape_names[indices[1]]
    Shape2_file_name  = possible_file_names[indices[1]]
    Shape2_msg = "Shape 2 is: " + Shape2_shape_name
    Shape3_shape_name = possible_shape_names[indices[2]]
    Shape3_file_name  = possible_file_names[indices[2]]
    Shape3_msg = "Shape 3 is: " + Shape3_shape_name

    # make mismatched pairs
    mismatch_labels =         list(possible_labels[i] for i in [1,2])
    mismatch_shape_name =     list(possible_shape_names[i] for i in [1,2])
    mismatch_shape_filename = list(possible_file_names[i] for i in [1,2])
    random.shuffle(mismatch_labels)
    random.shuffle(mismatch_shape_name)
    random.shuffle(mismatch_shape_filename)
    # mis pair 1
    m1label = mismatch_labels[0]
    m1shape = mismatch_shape_name[0]
    m1fname = mismatch_shape_filename[0]
    # mis pair 2
    m2label = mismatch_labels[1]
    m2shape = mismatch_shape_name[1]
    m2fname = mismatch_shape_filename[1]

elif the_current_task == "valence":
    # then 
    possible_labels=['happy', 'neutral', 'sad']
    random.shuffle(possible_labels)
    Label1_type = possible_labels[0]
    Label1_type_msg = "Label 1 is: " + Label1_type
    Label2_type = possible_labels[1]
    Label2_type_msg = "Label 2 is: " + Label2_type    
    Label3_type = possible_labels[2]
    Label3_type_msg = "Label 3 is: " + Label3_type

    indices=[0,1,2]
    random.shuffle(indices)
    possible_file_names =  ['H.bmp', 'R.bmp', 'X.bmp']
    possible_shape_names = ['Hexagon',     'Rectangle',     'Star']

    Shape1_shape_name = possible_shape_names[indices[0]] 
    Shape1_file_name  = possible_file_names[indices[0]] 
    Shape1_msg = "Shape 1 is: " + Shape1_shape_name
    Shape2_shape_name = possible_shape_names[indices[1]]
    Shape2_file_name  = possible_file_names[indices[1]]
    Shape2_msg = "Shape 2 is: " + Shape2_shape_name
    Shape3_shape_name = possible_shape_names[indices[2]]
    Shape3_file_name  = possible_file_names[indices[2]]
    Shape3_msg = "Shape 3 is: " + Shape3_shape_name

thisExp.addData('subjectNumber', p)

thisExp.addData('task', the_current_task)

thisExp.addData('Label1_type', Label1_type)
thisExp.addData('Shape1_shape_name', Shape1_shape_name)
thisExp.addData('Shape1_file_name', Shape1_file_name)

thisExp.addData('Label2_type', Label2_type)
thisExp.addData('Shape2_shape_name', Shape2_shape_name)
thisExp.addData('Shape2_file_name', Shape2_file_name)

thisExp.addData('Label3_type', Label3_type)
thisExp.addData('Shape3_shape_name', Shape3_shape_name)
thisExp.addData('Shape3_file_name', Shape3_file_name)
