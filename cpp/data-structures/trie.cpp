#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;


class TrieNode {
	public:
		TrieNode(char v) {
			val = v;			
		}
		char val;
		bool isword;		
		unordered_map<char, TrieNode*> children;
		void addValue(string v, int idx) {					
			if (children.find(v[idx]) == children.end()) {
				children[v[idx]] = new TrieNode(v[idx]);				
			}
			if (v.length()-1 > idx) {
				children[v[idx]]->addValue(v, idx+1);
			}
			else {
				children[v[idx]]->isword = true;
			}
		}
		void debug() {
			cout << val << " " << isword << endl;
			  for(unordered_map<char, TrieNode*>::iterator iter = children.begin(); iter != children.end(); ++iter){
		        iter->second->debug();		        
		    }			
		}
		~TrieNode() {

			for(unordered_map<char, TrieNode*>::iterator iter = children.begin(); iter != children.end(); ++iter){
		        delete iter->second;		        
		    }			
		}

};

class Trie {
	public:
		unordered_map<char, TrieNode*> roots;
		Trie() {
			
		}

		void addValue(string val) {
			for(int i = 0; i < val.length(); i++) {
				val[i] = tolower(val[i]);
			}
			
			if (roots.find(val[0]) == roots.end()) {
				roots[val[0]] = new TrieNode(val[0]);							
			}
			roots[val[0]]->addValue(val, 1);
		}	

		void debug() {			
			for(unordered_map<char, TrieNode*>::iterator iter = roots.begin(); iter != roots.end(); ++iter){
		        iter->second->debug();		        
		    }	
			cout << endl;
		}

		~Trie() {			

			for(unordered_map<char, TrieNode*>::iterator iter = roots.begin(); iter != roots.end(); ++iter){
		        delete iter->second;		        
		    }	
		}	
};




int main() {
	Trie mytrie;
	
	mytrie.addValue("Hey");
	mytrie.addValue("fey");
	mytrie.addValue("gey");
	mytrie.addValue("eey");
	mytrie.addValue("wey");
	mytrie.debug();
	
	return 0;
}