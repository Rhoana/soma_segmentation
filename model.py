import tensorflow as tf
from parameters import *

# convolutional layer
def conv2d(inputs , filters):
    out = tf.nn.conv2d( inputs , filters , strides=1 , padding="SAME" )
    return tf.nn.relu(out)

# transposed convolutional layer
def conv2d_T(inputs , filters):
    strides = 2
    output_shape_ = inputs.shape.as_list()
    output_shape_[1]=output_shape_[1]*strides
    output_shape_[2]=output_shape_[2]*strides
    output_shape_[3]=filters.shape[2]
    out = tf.nn.conv2d_transpose( inputs , filters, output_shape=output_shape_, strides=2 , padding="SAME" )
    return tf.nn.relu(out)

# max pool layer of size 2
def maxpool2(inputs):
    return tf.nn.max_pool2d( inputs , ksize=2 , padding="SAME" , strides=2 )

@tf.function
def model(L11, weights) :
    L12 = conv2d(L11, weights.values[0])
    L13 = conv2d(L12, weights.values[1])

    L21 = maxpool2(L13)
    L22 = conv2d(L21, weights.values[2])
    L23 = conv2d(L22, weights.values[3])

    L31 = maxpool2(L23)
    L32 = conv2d(L31, weights.values[4])
    L33 = conv2d(L32, weights.values[5])

    L41 = maxpool2(L33)
    L42 = conv2d(L41, weights.values[6])
    L43 = conv2d(L42, weights.values[7])

    L51 = maxpool2(L43)
    L52 = conv2d(L51, weights.values[8])
    L53 = conv2d(L52, weights.values[9])

    L44_ = conv2d_T(L53, weights.values[10])
    L44 = tf.concat([L43,L44_],axis=3)
    L45 = conv2d(L44, weights.values[11])
    L46 = conv2d(L45, weights.values[12])

    L34_ = conv2d_T(L46, weights.values[13])
    L34 = tf.concat([L33,L34_],axis=3)
    L35 = conv2d(L34, weights.values[14])
    L36 = conv2d(L35, weights.values[15])

    L24_ = conv2d_T(L36, weights.values[16])
    L24 = tf.concat([L23,L24_],axis=3)
    L25 = conv2d(L24, weights.values[17])
    L26 = conv2d(L25, weights.values[18])

    L14_ = conv2d_T(L26, weights.values[19])
    L14 = tf.concat([L13,L14_],axis=3)
    L15 = conv2d(L14, weights.values[20])
    L16 = conv2d(L15, weights.values[21])

    L17 = conv2d(L16, weights.values[22])

    return tf.nn.sigmoid(L17)
