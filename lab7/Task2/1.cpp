#include <bits/stdc++.h>
#define all(a) (a).begin(), (a).end()
using namespace std;
#define int long long
#define cyes cout << "YES" << '\n'
#define cno cout << "NO" << '\n'
#define pb push_back
#define fi first
#define se second
#define endl '\n'
void solve() {
    int n, c, k;
    cin >> n >> c >> k;
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    sort(all(a));
    for (int i = 0; i < n; i++) {
        if (a[i] <= c) {
            int e = c - a[i];

            if (k - e > 0){
              a[i] += e;
              k -= e;
              c += a[i];
            } 
            else {c += e - k; k -= e;}
            //cout << "e=" << " " << e << " " << "k=" << k << endl;
        } 
        else {
            break;
        }
        //cout << c << endl;
    }

    cout << c << endl;
}
signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int tt = 1;
    cin >> tt;
    while (tt--)solve();
}
