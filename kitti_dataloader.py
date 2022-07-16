import numpy as np
import glob

basedir='./dataset/sequences'
scenes=glob.glob(f'{basedir}/*')
nums=0
pairnums=0
for scene in scenes:
    fns=glob.glob(f'{scene}/velodyne/*.bin')
    nums+=(len(fns)-1)

fns=glob.glob(f'{scenes[0]}/velodyne/*.bin')
data=np.fromfile(fns[0],dtype=np.float32).reshape([-1,4])
i=0
for fn in fns[1:]:
    data=np.concatenate([data,np.fromfile(fn,dtype=np.float32).reshape([-1,4])],axis=0)
    print(data.shape)
np.savetxt('./data.txt',data,delimiter=',')
