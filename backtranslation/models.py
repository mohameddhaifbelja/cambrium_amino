from django.db import models
import json
import numpy as np
# Create your models here.
class Amino(models.Model):

    def backtranslate(self,seq):
        a = open('backtranslation/aminos.json')
        data = json.load(a)
        a.close()
        token = seq
        result=''
        error=''
        for j, c in enumerate(seq):
            if c.lower() not in list(data.keys()):
                error = "Invalid Amino Acid {} at index {} ".format(c.upper(), j)
                return False, error
            elm = data[c.lower()]
            #Generate random number between 0 and 1 
            x = np.random.rand()
            for i, p in enumerate(elm['probs']):
                if x > p:
                    break
            result += elm['neucs'][i]
        return True, result