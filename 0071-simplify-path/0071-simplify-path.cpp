class Solution {
public:
    string simplifyPath(string path) {
        stack<string> paths;

        // Traverse through the path
        for (int i=0; i<path.size(); i++)
        {
            // Don't do anything if at "/"
            if (path[i]=='/')
                continue;
            
            // Use sub_path to store path between "/"
            string sub_path = "";
            while (i<path.size() && path[i]!='/')
            {
                sub_path += path[i];
                i++;
            }

            // Don't do anything if sub_path=="."
            if (sub_path==".")
                continue;
            // Pop paths if sub_path==".." when paths is not empty
            else if (sub_path=="..")
            {
                if (!paths.empty())
                    paths.pop();
            }
            else
                paths.push(sub_path);
        }

        string ans = "";
        // Since stack if FILO, so we add the top to the front of ans
        while (!paths.empty())
        {
            ans = "/" + paths.top() + ans;
            paths.pop();
        }

        if (ans.size()==0)
            return "/";
        return ans;
    }
};