from datetime import datetime

def log_level(f_name):
    def decor_level(func_name):
        def wrap_level(*var_):
            with open(f_name, 'a') as f:
                f.write("{}:f={} get param=".format(datetime.now(),func_name))
                for par_ in var_[1:]:
                    f.write("[{}]".format(par_))
                result = func_name(*var_)
                f.write(" result={}\n".format(str(result)))
            return result
        return wrap_level
    return decor_level


class MainClass:

    @log_level("log_pr")
    def __init__(self, max_val, test_opt):
        self.max_val = max_val
        self.test_opt= test_opt

    @log_level("log_pr")
    def get_triple(self,val):
        result =[]
        for v1 in range(1,val-1):
            for v2 in range(v1,(val-v1)/2+1):
                result.append((v1,v2,val-v1-v2))
        return result
    def get_all(self):
        result=[]
        for i in range(self.max_val+1):
            #r=self.get_triple(i)
            #if len(r):
            result.append(self.get_triple(i))
            '''print("i={} len={} |{}".format(i,len(result),result))
            URA--+++
            for r_ in result:
                for rr_ in r_:
                    print("!{}!".format(sum(rr_)))
                    '''
        return result



if __name__ =="__main__":
    main_obj = MainClass(20,'just test')
    #for i in main_obj.get_triple():
    print(main_obj.get_all())
