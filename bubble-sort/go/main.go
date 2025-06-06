package main

import "fmt"

func bubble_sort(arr []int) []int {
	n := len(arr)

	for i := 0; i < n-1; i++ {
		swapped := false
		for j := 0; j < n-i-1; j++ {
			if arr[j] > arr[j+1] {
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = true
			}
		}
		if !swapped {
			break
		}
	}
	return arr
}

func main() {
	a := []int{3, 30, 6, 45, 9, 1}
	fmt.Printf("%+v\n", bubble_sort(a))
}
