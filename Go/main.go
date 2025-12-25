package main
import (
	"fmt"
	"strings"
	)

func main() {
	running := true

	var quit string

	fmt.Println("Hello welcome to calc")
	for running {
		fmt.Print("Do you want to quit: ")
		fmt.Scan(&quit)
		quit = strings.ToLower(strings.TrimSpace(quit))
		if quit == "yes" || quit == "y" {
			fmt.Println("/n Exiting...")
			running = false
		} else if quit == "no" || quit == "n" {

		}

	}
}

