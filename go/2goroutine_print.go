package main

var globleMap map[string]interface{}

func MapEdit(key string) {
	for i := 0; i < 10000; i++ {
		globleMap[key] = i
	}
}

func main() {
	globleMap = make(map[string]interface{})
	go MapEdit("1")
	//go MapEdit("2")
	//time.Sleep(time.Second * 30)
}
