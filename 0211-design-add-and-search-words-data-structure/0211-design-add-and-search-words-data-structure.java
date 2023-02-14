class TrieNode{
    private TrieNode[] children;
    private boolean endOfWord;

    public TrieNode(){
        children = new TrieNode[26];
        endOfWord=false;
    }

    public void setFinal(){
        endOfWord=true;
    }

    public boolean getFinal(){
        return endOfWord;
    }

    public boolean contains(char c){
        return children[c-'a']!=null;
    }

    public TrieNode get(char c){
        return children[c-'a'];
    }

    public void put(char c){
        children[c-'a']=new TrieNode();
    }
}
class WordDictionary {

    TrieNode root;
    public WordDictionary() {
        root=new TrieNode();
    }
    
    public void addWord(String word) {
        TrieNode curr=root;
        for (char c:word.toCharArray()) {
            if (!curr.contains(c)) {
                curr.put(c);
            }
            curr=curr.get(c);
        }
        curr.setFinal();
    }
    
    public boolean search(String word) {
        TrieNode curr=root;
        return dfs(root, word, 0);
    }

    private boolean dfs(TrieNode root, String word, int index) {
        if (root==null) {
            return false;
        }

        if (index==word.length()) {
            return root.getFinal();
        }

        if (word.charAt(index)=='.') {
            for (int i=0; i<26; i++) {
                int tmp=i+'a';
                if (dfs(root.get((char) tmp), word, index+1)) {
                    return true;
                }
            }
            return false;
        }
        else {
            return dfs(root.get(word.charAt(index)), word, index+1);
        }
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */