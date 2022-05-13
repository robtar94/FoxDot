# Cmajor = [C,D,E,F,G,A,B]
p1 >>  pluck([0,2,4], dur = [1, 1/2, 1/2], amp = 0.75) # 0,2,4 -- C,E,G , potem nuta i 2 polnuty.
p1.stop()

p2 >> pluck([0,1,2,3], dur = 2) + [0,0,4]
p2.stop()

# akord krotki
p3 >> pluck([0,1,2,3], dur = 2) + (0,2,4)
p3.stop()



