#!/usr/bin/env ruby
puts ARGV[0].scan(/(\W|^)hb(t){2,5}n(\W|$)/).join
