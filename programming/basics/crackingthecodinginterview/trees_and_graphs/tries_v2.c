// https://www.techiedelight.com/trie-implementation-insert-search-delete/?__cf_chl_captcha_tk__=cc0b36fd711d4dd1ade0edae3d63989b359382f9-1590247394-0-AfoxIXhFzPtniHWsy3ixZbj3jsk6k89IPdCEKNVZqIj7F_z4P1Ijra1EHtXEOZMX098526jTcpSl1jhoGo2wUKoYyJWTYZJfVmf8CpgQs8HZUpKQHyMu15g-SKOxKjeoBRK4LrhtMByN9YyqD25NBX2UzwgxVCql1qr28_n-E4NYf0Idg6Uhk118KIkJ6ea1eYVAkNv1Q8p36oW7a94t8qjZkc3Th9eo72XqJURrnjzVBc1xBorXlzS5r9DTJ8rAjvtniwlyW29zpC_LPNk9MnP-jR-8OOPhboLv0VMymHpqw8rYHxXotN1gaZb1jEc5OL_vt8hWR8h2z0VE-OzB22hZh7AbnZR8YlCVtXPx93YXYmVKIZKIq0QuTTZBLXT2IL4APEI4o0rXDnVvfWhHea22UeQhk9_gkkOW2C9DjOH-VIFZ4ObK1WQfnjZ6tqPMlrvTNpQrWoxH2VvJRkJUVYxGuMfAH_vdfRurvWl46ASmQaXLVp0ptCzeVkM9IAz2aWNKQM1RxBadueQ-UIcxsxcekJYp2-s-G-caWRBN_kRc
// https://www.geeksforgeeks.org/trie-insert-and-search/
// https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-less-than-100-lines-of-code-a877ea23c1a1
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define ALPHABET_SIZE 26

typedef struct tries_node {
    char c;
    bool end_of_word;
    int n_children;
    struct tries_node *children[ALPHABET_SIZE];
} tries_node;


tries_node *tries_create_node() {
    int i = 0;
    tries_node *n = malloc(sizeof(tries_node));
    if (!n) {
        perror("failed to malloc\n");
        exit(-1);
    }
    n->end_of_word = false;
    n->n_children = 0;
    for (i = 0; i < ALPHABET_SIZE; i++) {
        n->children[i] = NULL;
    }
    return n;
}

void tries_insert(tries_node *root, const char *str) {
    int s_len = strlen(str);
    tries_node *ptr = root;
    int i = 0, ch_idx = 0;

    if (!root) return;

    for (i = 0; i < s_len; i++) {
        ch_idx = (int)(str[i] - 'a');
        if (ptr->children[ch_idx] == NULL) {
            ptr->children[ch_idx] = tries_create_node();
            ptr->children[ch_idx]->c = str[i];
            ptr->n_children += 1;
        }
        ptr = ptr->children[ch_idx];
    }
    ptr->end_of_word = true;
}

bool tries_search(tries_node *root, const char *str) {
    int s_len = strlen(str);
    tries_node *ptr = root;
    int i = 0, ch_idx = 0;

    if (!root) return false;

    for (i = 0; i < s_len; i++) {
        ch_idx = (int)(str[i] - 'a');
        if (ptr->children[ch_idx] == NULL) {
            return false;
        }
        ptr = ptr->children[ch_idx];
    }

    return ptr->end_of_word;
}

void tries_delete(tries_node *root, const char *str) {
    int ch_idx = 0;
    
    if (!root) return;

    ch_idx = str[0] - 'a';
    if (root->children[ch_idx]) {
        tries_delete(root->children[ch_idx], str+1);
        if (!root->children[ch_idx]) {
            root->n_children--;
        }
    }
    if (root->n_children == 0) {
        free(root);
        root = NULL;
    }
}

int main() {
    tries_node *head = tries_create_node();
    tries_insert(head, "frank");
    printf("frank: %d\n", tries_search(head, "frank"));
    printf("fran: %d\n", tries_search(head, "fran"));
    printf("franky: %d\n", tries_search(head, "franky"));
    tries_insert(head, "franosuke");
    printf("frank: %d\n", tries_search(head, "frank"));
    printf("franosuke: %d\n", tries_search(head, "franosuke"));
    printf("fran: %d\n", tries_search(head, "fran"));
    printf("franosukes: %d\n", tries_search(head, "franosukes"));
    tries_insert(head, "frog");
    printf("frog: %d\n", tries_search(head, "frog"));
    tries_delete(head, "fro");
    printf("frog: %d\n", tries_search(head, "frog"));
    return 0;
}
