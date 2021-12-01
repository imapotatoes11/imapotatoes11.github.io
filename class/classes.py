class ee:
    def __init__(self):
        return
    def stop(self=None):
        import sys
        sys.exit()
    def count(upto=100, countInterval=1, startAt=0):
        while startAt!=upto:
            startAt=startAt+countInterval
            print(startAt)
        print("Done!")
    def randd(integerNumberOfBytesToOutput=128):
        import random as r
        print(r.randbytes(integerNumberOfBytesToOutput))