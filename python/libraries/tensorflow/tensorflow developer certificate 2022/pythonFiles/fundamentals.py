#
# Purpose : To Experiment with Tensors
#

#
# Purpose : To Experiment with Tensors
#
import tensorflow as tf

tensorContainer = []

def describe_tensor(tensor: tf.Tensor) -> None:
    """ Describe a tensor by printing the shape, dimensions and size. """
    string = "for the following tensor: "
    string += "shape =" + str(tf.shape(tensor))
    string += " dimensions = " + str(tensor.ndim)
    string += " size = " + str(tf.size(tensor))
    print(string)

def create_random_tensor() -> tf.Tensor:
    tf.random.set_seed(12)
    return tf.random.normal(shape=(5, 300))

#
# Create a scalar
#
scalar1 = tf.constant(7)
tensorContainer.append(scalar1)

print("scalar 1 = ", scalar1)

#
# Create a vector
#
vector1 = tf.constant([8, 9])
tensorContainer.append(vector1)

print("vector 1 = ", vector1)

#
# Create a matrix
#
matrix1 = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
tensorContainer.append(matrix1)

print("matrix 1 = ", matrix1)

#
# Create a tensor
#
tensor1 = tf.constant([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]])
tensorContainer.append(tensor1)

print("tensor 1", tensor1)

#
# Print the shape, rank, dimensions and size of the tensors
#
for item in tensorContainer:
    describe_tensor(item)

#
# Create two tensors containing random values between 0 and 1 with shape.
#
randomTensor1 = create_random_tensor()
randomTensor2 = create_random_tensor()

print(randomTensor1)
print(randomTensor2)

#
# Multiply the two randomly created tensors using Matrix Multiplication and Dot Product
#
matrix_mult_1 = tf.linalg.matmul(randomTensor1, tf.transpose(randomTensor2))
matrix_mult_2 = tf.linalg.tensordot(randomTensor1, tf.transpose(randomTensor2), axes=1)
print(matrix_mult_1 == matrix_mult_2)

#
# Create a tensor with random values between 0 and 1 with shape 224,224,3
#
minMaxValues_1 = tf.random.Generator.from_seed(42)
minMaxValues_1 = tf.random.normal(shape=(224, 224, 3))
print("The shape     of minMaxValue_1 = ", tf.shape(minMaxValues_1))
print("The min value of minMaxValue_1 = ", tf.reduce_min(minMaxValues_1))
print("The max value of minMaxValue_1 = ", tf.reduce_max(minMaxValues_1))
print("The maxtrix is ", minMaxValues_1)

#
# Create a matrix of shape=1,224,224,3 then squeeze it to change the shape to [224,224,3]
#
squeeze_matrix_1 = tf.random.normal(shape=(1,224,224,3))
print("The shape of squeeze_matrix_1 is ", tf.shape(squeeze_matrix_1))
squeeze_matrix_2 = tf.squeeze(squeeze_matrix_1)
print("The shape of squeeze_matrix_2 is ", tf.shape(squeeze_matrix_2))

#
# Create a tensor with shape 10 using your own choice of values then find the index which has
# the maximum value.
#
shape10Tensor = tf.constant([0, 1, 2, 3, 14, 5, 6, 7, 8, 9])
print("The shape of shape10Tensor = ", tf.shape(shape10Tensor))
print("The index with the max value is ", tf.argmax(shape10Tensor))

#
# Create a one hot encode from tensor created in 9
#
oneHotTensor = tf.one_hot(shape10Tensor, tf.reduce_max(shape10Tensor) + 1)
print("The One Hot Tensor is ", oneHotTensor)

