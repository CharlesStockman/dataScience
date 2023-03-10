def tensor_to_string(tensor):
    print("Information on the tensor ********************\n")
    print("Datatype:                     ", tensor.dtype)
    #print("Dimensions                    ", tensor.)
    print("Dimensions                    ", tensor.rank(tensor))
    print("Shape                         ", tensor.shape)
    print("Total Number of elements      ", tensor.size(tensor))
    print("Elements along the X Axis     ", tensor.shape[0])
    print("Elements alongs the last Axis ", tensor.shape[-1])
    print("End ********************************************\n")