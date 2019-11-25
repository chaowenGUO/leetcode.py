class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        std::size_t index{0};
        std::for_each(std::cbegin(nums), std::cend(nums), [&](auto const num){
            if (num != val)
            {
                nums.at(index) = num;
                ++index;}});
        return index;
    }
};
