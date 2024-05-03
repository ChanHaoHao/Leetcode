class Solution {
public:
    int compareVersion(string version1, string version2) {
        int size1=version1.size(), size2=version2.size();
        int left1=0, right1=0, left2=0, right2=0;

        while (left1<size1 && left2<size2)
        {
            while (right1<size1 && version1[right1]!='.')
            {
                right1++;
            }
            // get the substring between '.', substr(start, length)
            string sub_ver1=version1.substr(left1, right1-left1);
            left1 = right1+1;
            right1 = left1+1;

            while (right2<size2 && version2[right2]!='.')
            {
                right2++;
            }
            string sub_ver2=version2.substr(left2, right2-left2);
            left2 = right2+1;
            right2 = left2+1;

            if (stoi(sub_ver1)>stoi(sub_ver2))
                return 1;
            else if (stoi(sub_ver1)<stoi(sub_ver2))
                return -1;
        }

        // if left1 still has something
        while (left1<size1)
        {
            while (right1<size1 && version1[right1]!='.')
            {
                right1++;
            }
            string sub_ver1=version1.substr(left1, right1-left1);
            printf("%s\n", sub_ver1.c_str());
            if (stoi(sub_ver1))
                return 1;
            left1 = right1+1;
            right1 = left1+1;
        }
        while (left2<size2)
        {
            while (right2<size2 && version2[right2]!='.')
            {
                right2++;
            }
            string sub_ver2=version2.substr(left2, right2-left2);
            if (stoi(sub_ver2))
                return -1;
            left2 = right2+1;
            right2 = left2+1;
        }

        return 0;
    }
};