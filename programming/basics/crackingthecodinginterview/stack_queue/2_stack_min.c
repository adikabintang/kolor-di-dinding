// stack push pop min with O(1)
#include <stdio.h>
#include <stdbool.h>

#define STACK_SIZE 10

struct Data
{
    int value;
    int min_beneath_index;
};

typedef struct Data Data;

struct Stack
{
    Data data[STACK_SIZE];
    int top_index;
    int min_global_index;
    bool first_time;
};

typedef struct Stack Stack;

bool push(Stack *stack, int value)
{
    if (stack->first_time)
    {
        stack->top_index = -1;
        stack->min_global_index = 0;
        stack->first_time = false;
    }

    if (stack->top_index >= STACK_SIZE - 1)
    {
        return false;
    }
    else
    {
        (stack->top_index)++;
        Data *data = &(stack->data[stack->top_index]);
        data->value = value;
        data->min_beneath_index = stack->min_global_index;
        if (value < stack->data[stack->min_global_index].value)
        {
            stack->min_global_index = stack->top_index;
        }
    }
}

int pop(Stack *stack, int *err)
{
    if (stack->first_time)
    {
        *err = 1;
        return -1;
    }
    if (stack->top_index < 0)
    {
        *err = 1;
        return -1;
    }

    *err = 0;
    int val = stack->data[stack->top_index].value;
    if (stack->top_index == stack->min_global_index)
    {
        stack->min_global_index =
            stack->data[stack->top_index].min_beneath_index;
    }
    stack->top_index--;

    return val;
}

int peek(Stack *stack, int *err)
{
    if (stack->top_index < 0)
    {
        *err = 1;
        return -1;
    }

    *err = 0;
    return stack->data[stack->top_index].value;
}

int min(Stack *stack, int *err)
{
    if (stack->top_index < 0)
    {
        *err = 1;
        return -1;
    }

    *err = 0;
    return stack->data[stack->min_global_index].value;
}

int main()
{
    Stack s;
    s.first_time = true;

    push(&s, 8);
    push(&s, 6);
    push(&s, 5);
    push(&s, 12);

    int i, val, m, err, err_2, p, err_3;

    for (i = 0; i < 4; i++)
    {
        p = peek(&s, &err_3);
        m = min(&s, &err_2);
        val = pop(&s, &err);
        if (!err && !err_2)
        {
            printf("val: %d, min: %d\n", val, m);
        }
        else
        {
            printf("pop error: %d\n", err);
            printf("min error: %d\n", err_2);
        }
    }
}