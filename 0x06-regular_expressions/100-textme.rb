#!/usr/bin/env ruby
puts ARGV[0].scan(/from:[\d\w]+|to:[+\d]+|flags:[\S]{12}/).join
