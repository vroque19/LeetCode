function twoSum(nums: number[], target: number): number[] {
  let hmap = new Map<number, number>();
  for(let i = 0; i < nums.length; i++) {
      let diff = target - nums[i];
      if(diff in hmap && hmap[diff] != i) {
          return [hmap[diff], i];
      }
      hmap[nums[i]] = i;
  }
  return[]
};
