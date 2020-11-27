credits = list(map(int, input("Credits:").split()))
points = list(map(int, input("Points: ").split()))

def cal_gpa(cred, pts) :
    n = len(pts)
    var = 0

    for i in range(n) :
        var = var + credits[i]*pts[i]
    return var/sum(cred)

gpa = cal_gpa(credits, points)
print ("GPA = ",gpa)
