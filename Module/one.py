class one:
    def one():
        print("running one.py")
    def one_on_one():
        print("running one on one")

print("global printout")
# print(__name__)


if __name__=="__main__":
    l=one()
    l
else:
    print("class one is being imported")