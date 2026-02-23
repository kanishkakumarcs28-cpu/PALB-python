45.class Solution{
    int[] createFootpath(int n,int m,int[][] a,int q,int[][] queries){
        int[] ans=new int[q];
        for(int k=0;k<q;k++){
            int R=queries[k][0]-1;
            int C=queries[k][1]-1;
            int sum=0;
            int min1=Integer.MAX_VALUE;
            for(int i=0;i<R;i++)
                for(int j=0;j<C;j++)
                    min1=Math.min(min1,a[i][j]);
            if(min1!=Integer.MAX_VALUE) sum+=min1;
            int min2=Integer.MAX_VALUE;
            for(int i=0;i<R;i++)
                for(int j=C+1;j<m;j++)
                    min2=Math.min(min2,a[i][j]);
            if(min2!=Integer.MAX_VALUE) sum+=min2;
            int min3=Integer.MAX_VALUE;
            for(int i=R+1;i<n;i++)
                for(int j=0;j<C;j++)
                    min3=Math.min(min3,a[i][j]);
            if(min3!=Integer.MAX_VALUE) sum+=min3;
            int min4=Integer.MAX_VALUE;
            for(int i=R+1;i<n;i++)
                for(int j=C+1;j<m;j++)
                    min4=Math.min(min4,a[i][j]);
            if(min4!=Integer.MAX_VALUE) sum+=min4;
            ans[k]=sum;
        }
        return ans;
    }
}
