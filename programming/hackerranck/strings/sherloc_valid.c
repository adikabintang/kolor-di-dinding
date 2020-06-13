#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

char* isValid(char* s) {
    int map[26] = { 0 };
    int a = -1, b = -1, a_ctr = 0, b_ctr = 0, i = 0;
    char *yes = "YES", *no = "NO";
    char *c = s;
    while (*c != '\0') {
        map[*c - 'a']++;
        c++;
    }

    for (i = 0; i < 26; i++) {
        if (map[i] == 0)
            continue;
        
        if (a == -1 || map[i] == a) {
            a = map[i];
            a_ctr++;
        }
        else {
            if (b == -1 || map[i] == b) {
                b = map[i];
                b_ctr++;
            }
            else {
                return no;
            }

            // if ((a - 1 == 0 || b - 1 == 0) || abs(a - b) == 1) {
                
            // } 
            // else {
            //     return no;
            // }
        }
    }

    if (b > a) {
        
    }

    if (a_ctr * a > 1 && b_ctr * b > 1) {
        return no;
    }

    return yes;
}

int main() {
    char *s = "ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd";
    //assert(strcmp((const char*) isValid("aabbcd"), "NO") == 0);
    //assert(strcmp((const char*) isValid("aabbccddeefghi"), "NO") == 0);
    assert(strcmp((const char*) isValid("abcdefghhgfedecba"), "YES") == 0);
    assert(strcmp((const char*) isValid(s), "YES") == 0);
    assert(strcmp((const char*) isValid("aaaaabc"), "NO") == 0);
    
}
