class my_conv(object):
    def __init__(self, input_data, weight_data, stride, padding = 'SAME'):
        self.input = np.asarray(input_data, np.float32)
        self.weights = np.asarray(weight_data, np.float32)
        self.stride = stride
        self.padding = padding
    def my_conv2d(self):
        """
        self.input: c * h * w  # 输入的数据格式
        self.weights: c * h * w
        """
        [c, h, w] = self.input.shape
        [kc, k, _] = self.weights.shape  # 这里默认卷积核的长宽相等
        assert c == kc  # 如果输入的channel与卷积核的channel不一致即报错
        output = []
        # 分通道卷积，最后再加起来
        for i in range(c):  
            f_map = self.input[i]
            kernel = self.weights[i]
            rs = self.compute_conv(f_map, kernel)
            if output == []:
                output = rs
            else:
                output += rs
        return output
    def compute_conv(self, fm, kernel):
        [h, w] = fm.shape
        [k, _] = kernel.shape

        if self.padding == 'SAME':
            pad_h = (self.stride * (h - 1) + k - h) // 2
            pad_w = (self.stride * (w - 1) + k - w) // 2
            rs_h = h
            rs_w = w
        elif self.padding == 'VALID':
            pad_h = 0
            pad_w = 0
            rs_h = (h - k) // self.stride + 1
            rs_w = (w - k) // self.stride + 1
        elif self.padding == 'FULL':
            pad_h = k - 1
            pad_w = k - 1
            rs_h = (h + 2 * pad_h - k) // self.stride + 1
            rs_w = (w + 2 * pad_w - k) // self.stride + 1
        padding_fm = np.zeros([h + 2 * pad_h, w + 2 * pad_w], np.float32)
        padding_fm[pad_h:pad_h+h, pad_w:pad_w+w] = fm  # 完成对fm的zeros padding
        rs = np.zeros([rs_h, rs_w], np.float32)

        for i in range(rs_h):
            for j in range(rs_w):
                roi = padding_fm[i*self.stride:(i*self.stride + k), j*self.stride:(j*self.stride + k)]
                rs[i, j] = np.sum(roi * kernel) # np.asarray格式下的 * 是对应元素相乘
        return rs

if __name__=='__main__':
    input_data = [
        [
            [1, 0, 1, 2, 1],
            [0, 2, 1, 0, 1],
            [1, 1, 0, 2, 0],
            [2, 2, 1, 1, 0],
            [2, 0, 1, 2, 0],
        ],
        [
            [2, 0, 2, 1, 1],
            [0, 1, 0, 0, 2],
            [1, 0, 0, 2, 1],
            [1, 1, 2, 1, 0],
            [1, 0, 1, 1, 1],

        ],
    ]
    weight_data = [
        [
            [1, 0, 1],
            [-1, 1, 0],
            [0, -1, 0],
        ],
        [
            [-1, 0, 1],
            [0, 0, 1],
            [1, 1, 1],
        ]
    ]
    conv = my_conv(input_data, weight_data, 1, 'SAME')
    print(conv.my_conv2d())
