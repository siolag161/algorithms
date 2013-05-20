"""
An implemention of Knuth-Morris-Pratt algorithm in python...

More information about this algorithm could be found in: http://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm or in the famous Introduction to Algorithms Book

"""

class KMP:
    """ 
    this class is used to 2 versions of this algorithms: MP and KMP
    """

    
    def search_MP(self, s, p):
        """ 
        first version: the Morris-Pratt  return all the occurences        
        """
        results = []
            
            # mp = self.compute_KMP_map(p)
        mp = self.build_KMP_Map(p)

        ls = len(s);  lp = len(p);

        i = 0         
        for j in range(ls):            
            while (i>=0) and (s[j]!=p[i]):
                i = mp[i]
            i += 1
            if i == lp: #there's a match
                results.append(j-lp+1) # append to the result set
                i = 1 #restart 
        return results
            
    def build_MP_Map(self, p):
        """ it will build the MP-version border map used in the search function"""
        lp = len(p)
        mp = [-1]*(lp+1)
            
        for  i in range(lp):      
            j = mp[i]     
            while (j>=0) and (p[i]!=p[j]):
                j = mp[j]            
            mp[i+1] = j+1
        return mp

    def build_KMP_Map(self, p):
        lp = len(p)
        mp = [-1]*(lp+1)
        mp[1] = 0
        kmp = [-1]*(lp+1)
        kmp[1] = 0
        for i in range(1,lp-1):
            j = mp[i]            
            while (j >= 0) and (p[i] != p[j]):                
                j = mp[j]
            j = j+1
            mp[i+1] = j
            if (p[i+1] == p[j]):
                kmp[i+1] = mp[j]
            else:
                kmp[i+1] = j
        return kmp

   
