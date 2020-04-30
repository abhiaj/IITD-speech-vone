# -*- coding: utf-8 -*-
import warnings

from Location.census_utils import getEntityLocation
from Location.polyglot_utils import getLocation
from Location.utils import removeDuplicates, SortTuples
warnings.filterwarnings("ignore")

def get_loc(s):
    """
    Takes as input string s, outputs location identified in it
    """
    if (isinstance(s, str)) and (s.strip()!=""):
        polyglotLocation = getLocation(s)
        curloc = []
        for entity in polyglotLocation:
            curloc.append(getEntityLocation(entity))
        if curloc:
            curloc = SortTuples(curloc)
            curloc = removeDuplicates(curloc)
        min_alpha = 10000
        best_locs = []    
        for loc in curloc:
            if loc[0] != -1 and loc[0] <= min_alpha:
                min_alpha = loc[0]
                best_locs.append(loc)
        if len(best_locs) == 0:
            return [(-1, [], [], [], "")]
    else: 
        return [(-1, [], [], [], "")]
    return best_locs