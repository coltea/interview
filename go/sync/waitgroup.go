package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	var wg sync.WaitGroup
	wg.Add(2)
	number, letter := make(chan bool), make(chan bool)
	go func(w *sync.WaitGroup) {
		i := 0
		for {
			select {
			case <-number:
				if i == 10 {
					w.Done()
				} else if i < 10{
					fmt.Print(i)
				}
				i += 1
				letter <- true
			}
		}

	}(&wg)
	go func(w *sync.WaitGroup) {
		letterList := "abcdefghigkbjkfefefe"
		for {
			select {
			case <-letter:
				if len(letterList) > 0 {
					fmt.Print(letterList[:1])
					letterList = letterList[1:]
					number <- true
				} else {
					wg.Done()
				}

			}
		}

	}(&wg)
	start := time.Now()
	number <- true
	wg.Wait()
	println(time.Since(start))
}
