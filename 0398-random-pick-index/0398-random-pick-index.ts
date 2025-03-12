type Dict = {
    [key: number]: number[]; 
}

class Solution {
    private dict: Dict;
    private index: number;

    constructor(nums: number[]) {
        this.dict = {}; 
        this.index = 0;

        for (let i = 0; i < nums.length; i++) { 
            const num = nums[i]; 
            if (!this.dict[num]) { 
                this.dict[num] = []; 
            }
            this.dict[num].push(i);
        }
    }

    pick(target: number): number {
        const indices = this.dict[target];
        const randomIndex = indices[Math.floor(Math.random() * indices.length)]
        return randomIndex;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(nums);
 * var param_1 = obj.pick(target);
 */


