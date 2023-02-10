class Trie {

    ArrayList<String> list=new ArrayList();
    public Trie() {
        
    }
    
    public void insert(String word) {
        list.add(word);
    }
    
    public boolean search(String word) {
        return list.contains(word);
    }
    
    public boolean startsWith(String prefix) {
        boolean check=false;
        for (int i=0; i<list.size(); i++) {
            if (list.get(i).startsWith(prefix)) {
                check=true;
                break;
            }
        }
        return check;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */