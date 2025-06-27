#!/bin/bash
while true; do
  curl -s http://nginx-lb/work > /dev/null
  sleep 1
done
