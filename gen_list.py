import sys
import os

save_dir = "./data/12"
img_dir = "/lfs1/users/szhu/project/MTCNN-keras/data/"
if not os.path.exists(save_dir):
    os.mkdir(save_dir)
f1 = open(os.path.join(save_dir, 'pos_12.txt'), 'r')
f2 = open(os.path.join(save_dir, 'neg_12.txt'), 'r')
f3 = open(os.path.join(save_dir, 'part_12.txt'), 'r')

pos = f1.readlines()
neg = f2.readlines()
part = f3.readlines()
f = open(os.path.join(save_dir, 'label-train.txt'), 'w')

for i in range(int(len(pos))):
    p = pos[i].find(" ") + 1
    pos[i] = img_dir + pos[i][:p-1] + ".jpg " + pos[i][p:-1] + "\n"
    f.write(pos[i])

for i in range(int(len(neg))):
    p = neg[i].find(" ") + 1
    neg[i] = img_dir + neg[i][:p-1] + ".jpg " + neg[i][p:-1] + " -1 -1 -1 -1\n"
    f.write(neg[i])

for i in range(int(len(part))):
    p = part[i].find(" ") + 1
    part[i] = img_dir + part[i][:p-1] + ".jpg " + part[i][p:-1] + "\n" # add file attribute to the string
    f.write(part[i])

f1.close()
f2.close()
f3.close()