require 'fileutils'

f = File.open('data/plain-hosts', 'r')
out_file = 'data/new-hosts'
out = File.open(out_file, 'w')
f.each_line { |line| out.write line }

environment = ARGV[0]
if environment
  g = File.open("data/#{environment}-hosts", 'r')
  g.each_line { |line| out.write line }
end
out.close
f.close

FileUtils.cp(out_file, '/etc/hosts')