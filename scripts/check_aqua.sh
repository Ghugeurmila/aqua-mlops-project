#!/bin/bash
echo "Nagios Check: Verifying Port 5000..."
nc -zv localhost 5000 && echo "OK - Aqua Service is UP" || echo "CRITICAL - Service Down"
