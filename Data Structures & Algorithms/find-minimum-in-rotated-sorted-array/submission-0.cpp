class Solution {
public:
bool check(vector<int> &nums,int mid){
    if(nums[mid]-nums[0]>=0) return true;
    return false;
}
    int findMin(vector<int> &nums) {
        int n=nums.size();
        int low=0;
        int high=n-1;
        int ans=0;

        while(low<=high){
int mid=low+(high-low)/2;
cout<<check(nums,mid)<<" "<<nums[mid]<<"\n";
if(check(nums,mid)){
    low=mid+1;
}
else{
    ans=mid;
    high=mid-1;
}
        }
        return nums[ans];
    }
};
