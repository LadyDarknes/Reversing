#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    string input;
    const string table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    string result = "";

    cin >> input;
    vector<unsigned char> xor1;
    for (char c : input) {
        xor1.push_back(c ^ 0x5A);
    }

    int val = 0;
    int bits = 0;
    const unsigned int mess = 0x3F;
    for (unsigned char c : xor1) {
        val = (val << 8) | c;
        bits += 8;
        while (bits >= 6) {
            bits -= 6;
            result.push_back(table[(val >> bits) & mess]);
        }
    }

    if (bits > 0) {
        result.push_back(table[(val << (6 - bits)) & mess]);
    }
    while (result.size() % 4 != 0) {
        result.push_back('=');
    }

    cout << "Serial: " << result << endl;

    return 0;
}