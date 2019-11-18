#!/usr/bin/env ruby
match = ARGV[0].scan(/[A-Z]/)
string = match.join

puts string
