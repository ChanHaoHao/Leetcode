class Solution {
public:
    string simplifyPath(string path) {
        vector<string> sub_paths;
        string sub_path = "";

        for (auto & i: path)
        {
            if (i=='/')
            {
                if (sub_path.length()!=0)
                {
                    if (sub_path.length()==1 && sub_path=="."){}
                    else if (sub_path.length()==2 && sub_path=="..")
                    {
                        if (sub_paths.size()>0)
                        {
                            sub_paths.pop_back();
                        }
                    }
                    else
                    {
                        sub_paths.push_back(sub_path);
                    }
                    sub_path = "";
                }
            }
            else
                sub_path += i;
        }

        if (sub_path.length()==1 && sub_path=="."){}
        else if (sub_path.length()==2 && sub_path=="..")
        {
            if (sub_paths.size()>0)
                sub_paths.pop_back();
        }
        else if (sub_path.length()>0)
            sub_paths.push_back(sub_path);

        string ans = "/";
        for (auto & s: sub_paths)
        {
            cout << s << endl;
            ans += s + "/";
        }

        if (ans.length()>1)
            return ans.substr(0, ans.size()-1);
        return ans;
    }
};