package main

import (
	"crypto/tls"
	"fmt"
	"time"
)

type Server struct {
	Addr     string
	Port     int
	Protocol string
	Timeout  time.Duration
	MaxConns int
	TLS      *tls.Config
}

func Protocol(p string) func(*Server) {
	return func(s *Server) {
		s.Protocol = p
	}
}
func Timeout(timeout time.Duration) func(*Server) {
	return func(s *Server) {
		s.Timeout = timeout
	}
}
func MaxConns(maxConns int) func(*Server) {
	return func(s *Server) {
		s.MaxConns = maxConns
	}
}

func TLS(tls *tls.Config) func(*Server) {
	return func(s *Server) {
		s.TLS = tls
	}
}

func NewServer(addr string, port int, options ...func(*Server)) (*Server, error) {

	srv := Server{
		Addr:     addr,
		Port:     port,
		Protocol: "tcp",
		Timeout:  30 * time.Second,
		MaxConns: 1000,
		TLS:      nil,
	}

	for _, option := range options {
		option(&srv)
	}

	return &srv, nil
}

func main() {

	s1, _ := NewServer("localhost", 1024)
	s2, _ := NewServer("localhost", 2048, Protocol("udp"))
	s3, _ := NewServer("0.0.0.0", 8080, Timeout(300*time.Second), MaxConns(1000))
	fmt.Println(s1)
	fmt.Println(s2)
	fmt.Println(s3)
}
