package main
import (
	"fmt"
	"strings"
	)

func main() {
	running := true
	validari := true

	var quit string
	var ari string
	var arisym string

	var num1 int
	var num2 int
	var ans int

	fmt.Println("Hello welcome to calc")
	for running {
		fmt.Print("\nDo you want to quit: ")
		fmt.Scan(&quit)
		quit = strings.ToLower(strings.TrimSpace(quit))
		if quit == "yes" || quit == "y" {
			fmt.Println("\nExiting...")
			running = false
		} else if quit == "no" || quit == "n" {

			fmt.Print("\nEnter your first number: ")
			fmt.Scan(&num1)

			fmt.Print("\nEnter your second number: ")
			fmt.Scan(&num2)
			
			validari = true

			for validari {
				fmt.Print("\nWould you like to add, subtract, divide or multiply these numbers: ")
				fmt.Scan(&ari)
				
				switch ari {
					case "add":
						ans = add(num1, num2)
						validari = false
						arisym = "+"
					case "subtract":
						ans = subtract(num1, num2)
						validari = false
						arisym = "-"
					case "multiply":
						ans = multiply(num1, num2)
						validari = false
						arisym = "x"
					case "divide":
						ans = divide(num1, num2)
						validari = false
						arisym = "/"
					default:
						fmt.Println("Try Again")
				}
			}

			fmt.Printf("%v %v %v = %v\n", num1, arisym, num2, ans)
		}
	}

}