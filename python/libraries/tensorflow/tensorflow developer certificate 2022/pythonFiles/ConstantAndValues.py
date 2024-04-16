import tensorflow as tf
import numpy as np
import TensorToStringModule as func

#
# Print information

print("Showing one Value for constants and values")
scalarConstant = tf.constant(7);
scalarValue = tf.Variable(7);
print(scalarConstant)
print(scalarValue)
print("*******************************")

print("Showing a Vector for constants and values")
vectorConstant = tf.constant([10, 10])
vectorScalar = tf.Variable([10, 10]);
print(vectorConstant)
print(vectorScalar)
print("********************************")

print("Showing a matrix for constants and values ")
matrixConstant = tf.constant([[10, 7], [7, 10]])
matrixValue = tf.Variable([[10, 7], [7, 10]])
print(matrixConstant)
print(matrixValue)
print("********************************")

print ("Showing a Tensor for constants and values ")
tesnorConstant = tf.constant([[ [1,2,3],[4,5,6]], [[7,9,9], [10,11,12]], [[13,14,15], [16,17,18] ]])
tensorValue = tf.Variable([[ [1,2,3],[4,5,6]], [[7,9,9], [10,11,12]], [[13,14,15], [16,17,18] ]])
print(tesnorConstant)
print(tensorValue)
func.tensor_to_string(tensorValue)
print("********************************")

print("Modify a Variable in a Scalar Variable Type ")
print("The Original is ", scalarValue)
scalarValue.assign(8)
print("The New      is ", scalarValue)
print("********************************")

print("Modify a Variable in a Vector Variable Type  ")
print("The Original is ", vectorScalar)
vectorScalar[0].assign(2)
print("The new      is ", vectorScalar)
vectorScalar[1].assign(3)
print("The new      is ", vectorScalar)
print("********************************")

# print("Modify a Variable in a Matrix Variable Type")
# print("The Original is ", matrixValue)
# matrixValue.assign(matrixValue[0][0], [0])
# print("**", )
# print("The new is", matrixValue)
# print("The new is ", matrixValue)
# print("********************************")

print("Create a random tensor")

print(">>> With Seed 42")
tf.random.Generator.from_seed(420000)
random_1 = tf.random.normal([3, 2])
print(random_1)

print(">>> With Seed 43")
tf.random.Generator.from_seed(43)
random_2 = tf.random.normal([3,2])
print(random_2)

print(">>> With Seed 42 ")
tf.random.Generator.from_seed(420000)
random_3 = tf.random.normal([3, 2])
print(random_3)

# Create a vector and matrix of all ones
all_ones_vector = tf.ones([5,5])
print(all_ones_vector)

all_zeros_vector = tf.zeros(5,5)
print(all_zeros_vector)

# Turn Numpy Arrays into a vector and a matrix
numpy_array = np.arange(1, 25, 1, dtype='int16')
tensorflow_vector = tf.constant(numpy_array)
print(tensorflow_vector)
tensorflowTensor = tf.constant(numpy_array, shape=[2,3,4])
print(tensorflowTensor)




