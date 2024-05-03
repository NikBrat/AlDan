#include <stdio.h>
#include <vector>
using namespace std;

int main() {
    int n, k, index; scanf("%d %d",&n,&k); 
    vector<int> soldiers; 
    for (int i = 1; i < n+1; i++) soldiers.push_back(i); 
    k--; index = k; 
    for (--n; n > 0; n--) {
        printf("%d ", soldiers[index]); 
        soldiers.erase(soldiers.begin() + index); 
        index = (index + k) % (n); 
    }
    printf("%d ",soldiers[0]); 
    return 0; 
}
