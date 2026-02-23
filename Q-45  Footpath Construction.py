45.class Solution{
    int[] createFootpath(int n,int m,int[][] a,int q,int[][] queries){
        int[][] tl=new int[n][m];
        int[][] tr=new int[n][m];
        int[][] bl=new int[n][m];
        int[][] br=new int[n][m];
        
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                int val=a[i][j];
                if(i==0&&j==0) tl[i][j]=val;
                else if(i==0) tl[i][j]=Math.min(val,tl[i][j-1]);
                else if(j==0) tl[i][j]=Math.min(val,tl[i-1][j]);
                else tl[i][j]=Math.min(val,Math.min(tl[i-1][j],tl[i][j-1]));
            }
        }
        
        for(int i=0;i<n;i++){
            for(int j=m-1;j>=0;j--){
                int val=a[i][j];
                if(i==0&&j==m-1) tr[i][j]=val;
                else if(i==0) tr[i][j]=Math.min(val,tr[i][j+1]);
                else if(j==m-1) tr[i][j]=Math.min(val,tr[i-1][j]);
                else tr[i][j]=Math.min(val,Math.min(tr[i-1][j],tr[i][j+1]));
            }
        }
        
        for(int i=n-1;i>=0;i--){
            for(int j=0;j<m;j++){
                int val=a[i][j];
                if(i==n-1&&j==0) bl[i][j]=val;
                else if(i==n-1) bl[i][j]=Math.min(val,bl[i][j-1]);
                else if(j==0) bl[i][j]=Math.min(val,bl[i+1][j]);
                else bl[i][j]=Math.min(val,Math.min(bl[i+1][j],bl[i][j-1]));
            }
        }
        
        for(int i=n-1;i>=0;i--){
            for(int j=m-1;j>=0;j--){
                int val=a[i][j];
                if(i==n-1&&j==m-1) br[i][j]=val;
                else if(i==n-1) br[i][j]=Math.min(val,br[i][j+1]);
                else if(j==m-1) br[i][j]=Math.min(val,br[i+1][j]);
                else br[i][j]=Math.min(val,Math.min(br[i+1][j],br[i][j+1]));
            }
        }
        
        int[] ans=new int[q];
        for(int k=0;k<q;k++){
            int R=queries[k][0]-1;
            int C=queries[k][1]-1;
            int sum=0;
            if(R>0&&C>0) sum+=tl[R-1][C-1];
            if(R>0&&C<m-1) sum+=tr[R-1][C+1];
            if(R<n-1&&C>0) sum+=bl[R+1][C-1];
            if(R<n-1&&C<m-1) sum+=br[R+1][C+1];
            ans[k]=sum;
        }
        return ans;
    }
}
