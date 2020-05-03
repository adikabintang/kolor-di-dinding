#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

struct node
{
    char c;
    struct node *children;
    int children_size;
    bool end;
};

typedef struct {
    struct node *root;
} Trie;

/** Initialize your data structure here. */

Trie* trieCreate() {
    Trie *t = malloc(sizeof(Trie));
    t->root = malloc(sizeof(struct node));
    t->root->children_size = 0;
    return t;
}

/** Inserts a word into the trie. */
void trieInsert(Trie* obj, char * word) {
    struct node *ptr = obj->root;
    int i = 0;
    for (i = 0; i < strlen(word); i++)
    {
        bool found = false;
        int j = 0;
        if (ptr->children != NULL) {
            ptr = ptr->children;
            for (j = 0; j < ptr->children_size; j++)
            {
                if (ptr->c == word[i])
                {
                    found = true;
                    break;
                }
                ptr++;
            }
        }

        if (!found)
        {
            ptr->children = malloc(sizeof(struct node));
            ptr->children->c = word[i];
            ptr->children_size = 1;
            ptr = ptr->children;
        }
    }
    ptr->end = true;
}

/** Returns if the word is in the trie. */
bool trieSearch(Trie* obj, char * word) {
    struct node *ptr = obj->root;
    int i = 0;
    for (i = 0; i < strlen(word); i++)
    {
        bool found = false;
        int j = 0;
        struct node *child = ptr->children;
        for (j = 0; j < ptr->children_size; j++)
        {
            if (child->c == word[i])
            {
                ptr = child;
                found = true;
                break;
            }
            child++;
        }

        if (!found)
            return false;
    }

    return ptr->end == true;
}

/** Returns if there is any word in the trie that starts with the given prefix. */
bool trieStartsWith(Trie* obj, char * prefix) {
    struct node *ptr = obj->root;
    int i = 0;
    for (i = 0; i < strlen(prefix); i++)
    {
        bool found = false;
        int j = 0;
        struct node *child = ptr->children;
        for (j = 0; j < ptr->children_size; j++)
        {
            if (child->c == prefix[i])
            {
                ptr = child;
                found = true;
                break;
            }
            child++;
        }

        if (!found)
            return false;
    }

    return true;
}

void trieFree(Trie* obj) {
    
}

int main()
{
    char *word = "budj";
    char *prefix = "b";
    Trie* obj = trieCreate();
    trieInsert(obj, word);
 
    bool param_2 = trieSearch(obj, word);
    printf("-> %d\n", param_2);
 
    bool param_3 = trieStartsWith(obj, prefix);
    printf("-> %d\n", param_2);

    trieFree(obj);
    return 0;
}
/**
 * Your Trie struct will be instantiated and called as such:
 * Trie* obj = trieCreate();
 * trieInsert(obj, word);
 
 * bool param_2 = trieSearch(obj, word);
 
 * bool param_3 = trieStartsWith(obj, prefix);
 
 * trieFree(obj);
*/