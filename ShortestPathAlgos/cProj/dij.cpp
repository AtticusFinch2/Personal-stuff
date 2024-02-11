#include <stdio.h>
#include <string.h>
#include <vector>
#include <iostream>
#include <alg.h>
#include <queue>
#include <cstdint>
typedef long long ll;
using namespace std;
const int N = 2e5+3;
const ll inf = 1e16;
vector<vector<pair<ll,int>>> adj(N, vector<pair<ll,int>>());
vector<int> dist(N, inf);
 
void dijkstra() {
	dist[1] = 0;
	priority_queue<pair<ll, int>, vector<pair<ll,int>>, greater<pair<ll,int>>> pq;
	pq.push({0, 1});
	while(!pq.empty()) {
		ll d = pq.top().first; 
		ll u = pq.top().second; 
		pq.pop();
		if(dist[u] < d)
			continue;
		for(auto e : adj[u]) {
			ll v = e.second; 
			ll c = e.first; 
			if(dist[v] <= c+d) 
				continue;
			else {
				dist[v] = c+d;
				pq.push({dist[v], v});
			}
		}
	}
}
 
int32_t main() {
	int n, m;
	cin >> n >> m;
 
	for(int i = 1; i <= m; i++) {
		int a, b;
		ll w;
		cin >> a >> b >> w;
		adj[a].push_back({w, b});
	}
	dijkstra();
	for(int i = 1; i <= n; i++) {
		cout << dist[i] << " ";
	}
        return 0;
}
