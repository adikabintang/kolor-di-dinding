// https://golangbyexample.com/singleton-design-pattern-go/
package main

import (
	"fmt"
	"sync"
)

var once sync.Once

type single struct {
	member int
}

var singleInstance *single

func getInstance() *single {
	if singleInstance == nil {
		once.Do(
			func() {
				fmt.Println("creating a single insance")
				singleInstance = &single{}
			})
	}

	return singleInstance
}

func main() {
	fmt.Println("singleton demo")
	one := getInstance()
	two := getInstance()
	if one == two {
		fmt.Println("they are the same")
	}
}
