from bitarray import bitarray

import mmh3

class BloomFilter(set):
    def __init__(self,size,hash_count):
        #size:the num of the bitarray
        #hash_count:the num of hash function
        super(BloomFilter,self).__init__()
        self.bit_array = bitarray(size)
        self.bit_array.setall(0) #初始化为0
        self.size = size
        self.hash_count = hash_count

        def __len__(self):
            return self.size

        def __iter__(self):
            return iter(self.bit_array)

        def add(self,item):
            for i in range(self.hash_count):
                index = mmh3.hash(item,i) % self.size
                self.bit_array[index] = 1
            return self

        def __contains__(self,item):
            out = True
            for i in range(self.hash_count):
                index = mmh3.hash(item,i)%self.size
                if bit_array[index] == 0:
                    out = False
                    
            return out

def main():
    bloom = BloomFilter(100,5)
    fd = open("urls.txt")  #有重复的网址 http://www.kalsey.com/tools/buttonmaker/  
    bloomfilter = BloomFilter(100,10)    
    while True:    
        url = fd.readline().strip()   
        if (url == 'exit') :  
            print ('complete and exit now')
            break    
        elif url not in bloomfilter:   
            bloomfilter.add(url)
            # print(url)    
        else:    
            print ('url :%s has exist' % url )

if __name__ == '__main__':
        main()
