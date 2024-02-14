class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) 
    {
     vector<int >x,y,result;
     for(int i=0;i<nums.size();i++)
     {
         if (i<n)
         {
             x.push_back(nums[i]);
         }
         else
         {
             y.push_back(nums[i]);
         }
     }
     for(int i=0;i<n;i++)
     {
         result.push_back(x[i]);
         result.push_back(y[i]);

     }

     return result;

    }
};
