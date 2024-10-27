import numpy as np

def calculate(list):
    input = np.array(list)

    
    if len(input) < 9:
        raise ValueError ('List must contain nine numbers.')

    else:
        data = input.reshape((3,3))
        mean = np.mean(data, axis=0), np.mean(data, axis=1), np.mean(data)
        variance = np.var(data, axis=0), np.var(data, axis=1), np.var(data)
        standardiv = np.std(data, axis=0), np.std(data, axis=1), np.std(data)
        max = np.max(data, axis=0), np.max(data, axis=1), np.max(data)
        min = np.min(data, axis=0), np.min(data, axis=1), np.min(data)
        sum = np.sum(data, axis=0), np.sum(data, axis=1), np.sum(data)

        calculations = {'mean' : [mean[0].tolist(), mean[1].tolist(), mean[2].tolist()],
                        'variance' : [variance[0].tolist(), variance[1].tolist(), variance[2].tolist()],
                        'standard deviation': [standardiv[0].tolist(), standardiv[1].tolist(), standardiv[2].tolist()],
                        'max' : [max[0].tolist(), max[1].tolist(), max[2].tolist()],
                        'min' : [min[0].tolist(), min[1].tolist(), min[2].tolist()],
                        'sum' : [sum[0].tolist(), sum[1].tolist(), sum[2].tolist()]
        }
                                
                        

    return calculations
