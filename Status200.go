package main

import (
    "bufio"
    "fmt"
    "net/http"
    "os"
    "sync"
)

func checkDomain(domain string, wg *sync.WaitGroup, results chan<- string) {
    defer wg.Done()
    resp, err := http.Get("http://" + domain)
    if err == nil && resp.StatusCode == 200 {
        results <- domain
    }
}

func main() {
    if len(os.Args) != 2 {
        fmt.Println("Usage: go run check_list.go file_domain.txt")
        return
    }

    file, err := os.Open(os.Args[1])
    if err != nil {
        fmt.Printf("Error opening file: %v\n", err)
        return
    }
    defer file.Close()

    scanner := bufio.NewScanner(file)
    var wg sync.WaitGroup
    results := make(chan string, 100)

    for scanner.Scan() {
        domain := scanner.Text()
        wg.Add(1)
        go checkDomain(domain, &wg, results)
    }

    go func() {
        wg.Wait()
        close(results)
    }()

    fmt.Println("Domains with status code 200:")
    for domain := range results {
        fmt.Println(domain)
    }
}
