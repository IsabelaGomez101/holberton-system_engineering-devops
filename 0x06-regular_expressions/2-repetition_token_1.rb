#!/usr/bin/env ruby
puts ARGV[0].scan(/(\W|^)h{1}b{0,1}t{1}n{1}(\W|$)/).join
