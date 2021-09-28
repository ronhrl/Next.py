class UnderAge(Exception):
    def __init__(self, arg):
        self.args = arg

    def __str__(self):
        return "Your age is %s, which is under 18. In %d years you will be able to come" % (self.args, 18 - self.args)


def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(age)
        else:
            print("You should send an invite to " + str(name))
    except UnderAge as e:
        print(1)




def main():
    send_invitation(17, 20)


main()
