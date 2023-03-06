package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)

	a := make(map[string]struct{})

	for i := 0; i < n; i++ {
		var s string
		fmt.Scan(&s)
		a[s] = struct{}{}

	}

	fmt.Printf("%d\n", len(a))

}
