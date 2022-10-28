#include <iostream>
#include <string>
using namespace std;
string cipher(string word, int offset);
int main() {
    string word;
    int offset;

    cout << "Enter word/phrase: ";
    getline(cin, word);
    cout << "Enter offset: ";
    cin >> offset;

    word = cipher(word, offset);
    cout << "Ciphered word/phrase: " << word << endl;
}

string cipher(string word, int offset) {
    for (int i = 0; i < word.size(); i++) {
        for (int j = 0; j < offset; j++) {
            if (word[i] == ' ')
                continue;
            else if (word[i] == 'z') {
                word[i] = 'a';
                continue;
            }
            else if (word[i] == 'Z') {
                word[i] = 'A';
                continue;
            }
            else
                word[i]++;
        }
    }
    return word;
}