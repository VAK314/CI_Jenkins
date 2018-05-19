
class MainClass:
    def dec_l1(f_name):
            def dec_l2(func_name):
                def dec_l3(*var_):
                    with open(f_name, 'a') as f:
                        f.write("f={} get param=".format(f_name))
                        for par_ in var_:
                            f.write("[{}]".format(par_))
                        result = func_name(*var_)
                        f.write(" result={}\n".format(str(result)))
                    return result
                return dec_l3
            return dec_l2

    def __init__(self, max_val):
        self.max_val = max_val
    @dec_l1("log_pr")
    def get_triple(self,val):
        result =[]
        for v1 in range(1,val-1):
            for v2 in range(v1,(val-v1)/2+1):
                result.append((v1,v2,val-v1-v2))
        return result
    def get_all(self):
        for i in range(self.max_val+1):
            result  = self.get_triple(i)
            print("i={} len={} |{}".format(i,len(result),result))



if __name__ =="__main__":
    main_obj = MainClass(11)
    #for i in main_obj.get_triple():
    print(main_obj.get_all())
