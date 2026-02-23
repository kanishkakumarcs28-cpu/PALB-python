44.class Solution{
    ArrayList<Long> submatrixSum(long[][] a, int n, int m, int[][] query, int q){       
        long[][] prefix=new long[n][m];
        
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                long up=(i>0)?prefix[i-1][j]:0;
                long left=(j>0)?prefix[i][j-1]:0;
                long diag=(i>0&&j>0)?prefix[i-1][j-1]:0;
                prefix[i][j]=a[i][j]+up+left-diag;
            }
        }
        
        ArrayList<Long> ans=new ArrayList<>();
        
        for(int k=0;k<q;k++){
            int r1=query[k][0];
            int c1=query[k][1];
            int r2=query[k][2];
            int c2=query[k][3];
            
            long total=prefix[r2][c2];
            long above=(r1>0)?prefix[r1-1][c2]:0;
            long left=(c1>0)?prefix[r2][c1-1]:0;
            long overlap=(r1>0&&c1>0)?prefix[r1-1][c1-1]:0;
            
            ans.add(total-above-left+overlap);
        }
        
        return ans;
    }
}
