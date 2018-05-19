class MainClass:
    def __init__(self, sum_val):
        self.val = sum_val
    def get_triple(self):
        result =[range(self.val)]
        return result


if __name__ =="__main__":
    main_obj = MainClass(11)
    for i in main_obj.get_triple():
        print(i)
