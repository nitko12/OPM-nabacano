#include <iostream>
#include <vector>
using namespace std;

int n;
vector<vector<int>> adj, adj_t;
vector<bool> used;
vector<int> order, comp;
vector<bool> assignment;

void dfs1(int v)
{
    used[v] = true;
    for (int u : adj[v])
    {
        if (!used[u])
            dfs1(u);
    }
    order.push_back(v);
}

void dfs2(int v, int cl)
{
    comp[v] = cl;
    for (int u : adj_t[v])
    {
        if (comp[u] == -1)
            dfs2(u, cl);
    }
}

bool solve_2SAT()
{
    order.clear();
    used.assign(n, false);
    for (int i = 0; i < n; ++i)
    {
        if (!used[i])
            dfs1(i);
    }

    comp.assign(n, -1);
    for (int i = 0, j = 0; i < n; ++i)
    {
        int v = order[n - i - 1];
        if (comp[v] == -1)
            dfs2(v, j++);
    }

    assignment.assign(n / 2, false);
    for (int i = 0; i < n; i += 2)
    {
        if (comp[i] == comp[i + 1])
            return false;
        assignment[i / 2] = comp[i] > comp[i + 1];
    }
    return true;
}

void add_disjunction(int a, bool na, int b, bool nb)
{
    // na and nb signify whether a and b are to be negated
    a = 2 * a ^ na;
    b = 2 * b ^ nb;
    int neg_a = a ^ 1;
    int neg_b = b ^ 1;
    adj[neg_a].push_back(b);
    adj[neg_b].push_back(a);
    adj_t[b].push_back(neg_a);
    adj_t[a].push_back(neg_b);
}

int main()
{
    n = 10000;
    adj.resize(10000);
    adj_t.resize(10000);

    add_disjunction(0, 1, 1, 1);
    add_disjunction(2, 1, 3, 1);
    add_disjunction(4, 1, 5, 1);

    add_disjunction(0, 1, 4, 0);
    add_disjunction(1, 1, 4, 0);

    add_disjunction(2, 1, 5, 0);
    add_disjunction(3, 1, 5, 0);

    add_disjunction(4, 1, 6, 0);
    add_disjunction(5, 1, 6, 0);

    add_disjunction(6, 0, 6, 0);

    add_disjunction(0, 1, 0, 1);

    cout << solve_2SAT() << endl;

    for (int i = 0; i < 10; ++i)
        cout << assignment[i] << " ";
    cout << endl;

    for (int i = 0; i < 10; ++i)
        cout << i << " ";
    cout << endl;

    return 0;
}
