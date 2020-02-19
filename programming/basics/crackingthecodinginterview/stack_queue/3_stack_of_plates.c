// 3.3 stack of plates
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define STACK_SIZE 3
#define SET_SIZE 3

typedef struct stack
{
    int arr[STACK_SIZE];
    int top_idx;
} stack;

typedef struct set_of_stacks
{
    stack *st;
    int nth_stack;
} set_of_stacks;

set_of_stacks init_set_of_stack()
{
    set_of_stacks s;
    int i = 0;
    s.nth_stack = -1;
    s.st = (stack *)malloc(sizeof(stack) * SET_SIZE);
    for (i = 0; i < SET_SIZE; i++)
    {
        s.st[i].top_idx = -1;
    }

    return s;
}

bool push(set_of_stacks *ss, int value)
{
    if (ss->nth_stack >= SET_SIZE)
    {
        return false;
    }
    if (ss->nth_stack == -1 || ss->st[ss->nth_stack].top_idx >= STACK_SIZE - 1)
    {
        ss->nth_stack += 1;
    }
    stack *the_stack = &(ss->st[ss->nth_stack]);
    (*the_stack).top_idx++;
    (*the_stack).arr[(*the_stack).top_idx] = value;
    printf(" -- value %d pushed at %dnth stack and %dth top\n",
        value, ss->nth_stack, (*the_stack).top_idx);
    return true;
}

int peek(set_of_stacks ss, int *err)
{
    *err = 0;
    if (ss.nth_stack < 0)
    {
        *err = 1;
        return -1;
    }
    stack *the_stack = &(ss.st[ss.nth_stack]);
    return (*the_stack).arr[(*the_stack).top_idx];
}

int pop(set_of_stacks *ss, int *err)
{
    *err = 0;
    if (ss->nth_stack < 0)
    {
        *err = 1;
        return -1;
    }

    stack *the_stack = &(ss->st[ss->nth_stack]);
    int *top_index = &((*the_stack).top_idx);
    int val = (*the_stack).arr[*top_index];
    (*top_index)--;
    if (*top_index < 0)
    {
        ss->nth_stack--;
    }

    return val;
}

int main()
{
    int i = 0, err;
    set_of_stacks ss = init_set_of_stack();
    printf("push\n");
    for (i = 0; i < 9; i++)
    {
        if (push(&ss, i))
        {
            int val = peek(ss, &err);
            printf("peek: %d, err: %d\n", val, err);
        }
        else
        {
            printf("push error at: %d\n", i);
        }
    }

    printf("pop\n");
    for (i = 0; i < 6; i++)
    {
        int val = pop(&ss, &err);
        printf("pop: %d, err: %d\n", val, err);
    }
    
    return 0;
}