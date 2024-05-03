class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")

        min_length = min(len(version1), len(version2))
        i=0
        while i<min_length:
            if int(version1[i])<int(version2[i]):
                return -1
            elif int(version1[i])>int(version2[i]):
                return 1
            i+=1

        if len(version1)==len(version2):
            return 0
        elif len(version1)==min_length:
            while i<len(version2):
                if int(version2[i])!=0:
                    return -1
                i+=1
            return 0
        else:
            while i<len(version1):
                if int(version1[i])!=0:
                    return 1
                i+=1
            return 0