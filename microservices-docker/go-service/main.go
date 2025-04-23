package main

import (
	"fmt"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "Olá do serviço Go!")
}

func main() {
	http.HandleFunc("/", handler)
	fmt.Println("Servidor Go rodando na porta 8080...")
	http.ListenAndServe(":8080", nil)
}