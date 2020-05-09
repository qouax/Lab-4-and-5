import robopy.base.pose as pose

def main():
    # SE3: transformation or pose for x/y translation
    # rand(): generate random number
    x = pose.SE3.rand()
    y = pose.SE3.rand()

    z = x * y

    print(z)

if __name__ == '__main__':
    main()