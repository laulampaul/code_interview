
    def my_pooling(self):
        """
        self.input: c * h * w  # 输入的数据格式
        self.weights: c * h * w
        """
        [c, h, w] = self.input.shape
        [kc, k, _] = self.weights.shape  # 这里默认卷积核的长宽相等
        assert c == kc  # 如果输入的channel与卷积核的channel不一致即报错
        output = []
        # 分通道卷积，最后再concat
        for i in range(c):  
            f_map = self.input[i]
            kernel = self.weights[i]
            rs = self.avgpool2d(f_map, kernel)
            if output == []:
                output = rs
            else:
                output = torch.cat([output,rs],0)
        return output
      
    def avgpool2d(self, X, poolsize):
        p_h, p_w = pool_size
        Y = np.zeros((X.shape[0] - p_h + 1, X.shape[1] - p_w + 1))
        for i in range(Y.shape[0]):
            for j in range(Y.shape[1]):
                if mode == 'max':
                    Y[i, j] = X[i:i + p_h, j:j + p_w].max()
                elif mode == 'avg':
                    Y[i, j] = X[i:i + p_h, j:j + p_w].mean()
        return Y
      

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
    ## pooling
    conv = my_conv(input_data, weight_data, 1, 'SAME')
   
