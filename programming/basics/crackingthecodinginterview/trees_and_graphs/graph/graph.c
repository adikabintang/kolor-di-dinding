/**
https://www.programiz.com/dsa/graph-adjacency-list
https://www.programiz.com/dsa/graph-dfs

remember, in the adjacency list, the aim is to model the graph as something like 
this:
0: 3, 2, 1
1: 2, 0
2: 1, 0
3: 0

    1
  / |
0 - 2
  \
    3
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "queue_array.h"

#define CHECK_MALLOC(x) if (!x) { perror("failed to allocate\n"); exit(-1); }

// make it as a linked list
typedef struct node {
    int value;
    struct node *next;
} node;

typedef struct graph {
    int n_vertices;
    bool *visited; // just a flag for dfs/bfs
    node **adj_list;
} graph;

node *node_create(int val) {
    node *n = malloc(sizeof(node));
    CHECK_MALLOC(n)
    n->value = val;
    n->next = NULL;
    return n;
}

graph *graph_create(int n_vertices) {
    int i = 0;
    graph *g = malloc(sizeof(graph));
    CHECK_MALLOC(g)
    g->visited = malloc(n_vertices * sizeof(bool));
    CHECK_MALLOC(g->visited)
    g->n_vertices = n_vertices;
    g->adj_list = malloc(n_vertices * sizeof(node *));

    for (i = 0; i < n_vertices; i++) {
        g->adj_list[i] = NULL;
        g->visited[i] = false;
    }

    return g;
}

/**
 * See how the linked list is built and referenced to the graph->adj_list
 * note that this is both direction
 */
void add_edge(graph *g, int src, int dst) {
    // add an edge from src to dst
    node *s = node_create(src);
    s->next = g->adj_list[dst];
    g->adj_list[dst] = s;

    // add an edge from dst to src
    node *d = node_create(dst);
    d->next = g->adj_list[src];
    g->adj_list[src] = d;
}

void graph_print(graph *g) {
    int i = 0;
    node *ptr = NULL;
    for (i = 0; i < g->n_vertices; i++) {
        printf("%d: ", i);
        ptr = g->adj_list[i];
        while (ptr) {
            printf("%d, ", ptr->value);
            ptr = ptr->next;
        }
        printf("\n");
    }
}

void __dfs_helper(graph *g, int start_vertex) {
    if (!g) return;

    printf("%d, ", start_vertex);
    g->visited[start_vertex] = true;
    node *ptr = g->adj_list[start_vertex];
    while (ptr) {
        if (!g->visited[ptr->value]) {
            __dfs_helper(g, ptr->value);
        }
        ptr = ptr->next;
    }
}

void dfs(graph *g, int start_vertex) {
    int i = 0;
    for (i = 0; i < g->n_vertices; i++) {
        g->visited[i] = false;
    }
    __dfs_helper(g, start_vertex);
    for (i = 0; i < g->n_vertices; i++) {
        g->visited[i] = false;
    }
}

void __bfs_helper(graph *g, int start_vertex) {
    node *ptr = NULL;
    queue *q = q_create();
    int val = start_vertex;

    q_enqueue(q, val);
    g->visited[val] = true;
    while (!q_is_empty(q)) {
        if (q_dequeue(q, &val)) {
            printf("%d, ", val);
            ptr = g->adj_list[val];
            while (ptr) {
                val = ptr->value;
                if (!g->visited[val]) {
                    q_enqueue(q, val);
                    g->visited[val] = true;
                }
                ptr = ptr->next;
            }
        }
        else {
            perror("failed to dequeue\n");
            return;
        }
    }
}

void bfs(graph *g, int start_vertex) {
    int i = 0;
    for (i = 0; i < g->n_vertices; i++) {
        g->visited[i] = false;
    }
    __bfs_helper(g, start_vertex);
    for (i = 0; i < g->n_vertices; i++) {
        g->visited[i] = false;
    }
}

int main() {
    graph *g = graph_create(4);
    add_edge(g, 0, 1);
    add_edge(g, 0, 2);
    add_edge(g, 0, 3);
    add_edge(g, 1, 2);
    graph_print(g);
    printf("dfs: \n");
    dfs(g, 0);
    printf("\nbfs: \n");
    bfs(g, 0);
    return 0;
}