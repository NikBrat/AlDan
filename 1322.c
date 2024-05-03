#include <stdlib.h>
#include <stdio.h>
#include <stdint.h>
#include <math.h>
#include <string.h>

struct pair
/* структура с буковой и её индексом */
{
    uint32_t index;
    char ch;
};


int cmpd(const void* a, const void* b){
    /* функция для лексиграфической сортировки */
    struct pair* pair_a = (struct pair*) a;
    struct pair* pair_b = (struct pair*) b;

    if(pair_a -> ch > pair_b -> ch) return 1;
    if(pair_a -> ch < pair_b -> ch) return -1;

    return pair_a -> index - pair_b -> index; 
}

int main(void){
    /* считываем данные */
    size_t n;
    scanf("%zd", &n);
    n--;
    char* coded = malloc(sizeof(char) * 100010);
    scanf("%s", coded);
    
    uint32_t len = strlen(coded);

    struct pair* pairs = malloc(sizeof(struct pair) * len);
    /* заполняем массив парами индекс-символ */
    for(size_t i = 0; i < len; i++){
        pairs[i] = (struct pair) {.index = i, .ch = coded[i]};
    }
     /* лексиграфическая сортировка */
    qsort (pairs, len, sizeof(struct pair), cmpd);

    /* вывод результата */
    for(size_t i = 0; i < len; i++){
        n = pairs[n].index;
        printf("%c", coded[n]);
    }
    printf("\n");
}