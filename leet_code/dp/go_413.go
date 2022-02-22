package main

import (
	"fmt"
)

func main() {
	fmt.Println(numberOfArithmeticSlices([]int{1, 2, 3, 4}))
}

func numberOfArithmeticSlices(nums []int) int {
	count := 0
	if len(nums) < 3 {
		return count
	}

	for i := 2; i < len(nums); i++ {
		divValue := nums[i] - nums[i - 1]
		for j := i - 1; j >= 1; j-- {
			if nums[j] - nums[j - 1] == divValue {
				count += 1
			} else {
				break
			}
		}

	}
	return count

}
