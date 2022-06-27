/*int memoized_cut_rod( int *, int, int *)using dynamic-programming, improve the running time of the cut_rod.*/
int memoized_cut_rod( int *p, int n, int *ar){    int q, i, r;    // examine whether this problem is solved.   
 if( ar[n] >= 0)    
 {        return ar[n];    }    
 if( n == 0)    {        q   = 0;    }    else    {        q   = REVENUE;        for( i = 1 ; i <= n ; i ++)        {            // if the length of a rod is over the maximum revenue.            if( i >= PMAX)            {                r   = PMAX - 1;            }            else            {                r   = i - 1;            }            // call itself recursively to solve subproblems            q   = max( q, p[r] + memoized_cut_rod( p, n - i, ar));        }    }    ar[n]   = q; // save the result at this level.    return q;}
