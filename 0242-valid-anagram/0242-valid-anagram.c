bool isAnagram(char* s, char* t) {
    if (strlen(s) != strlen(t))
        return false;

    int count[26] = {0};

    for (int i=0; i<strlen(s); ++i) {
        count[s[i]-'a']++;
        count[t[i]-'a']--;
    }

    for (int i=0; i<26; ++i) {
        if (count[i] != 0)
            return false;
    }

    return true;
}