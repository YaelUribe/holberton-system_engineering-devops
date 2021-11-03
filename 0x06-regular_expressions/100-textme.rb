#!/usr/bin/env ruby
puts ARGV[0].scan(/(?<=from:)[\d\S]+|(?<=to:)[+\d]+|(?<=flags:)[-?[0-1]:]+/).join","
