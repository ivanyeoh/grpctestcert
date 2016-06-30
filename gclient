#!/usr/bin/env ruby

this_dir = File.expand_path(File.dirname(__FILE__))
lib_dir = File.join(this_dir, 'lib')
$LOAD_PATH.unshift(lib_dir) unless $LOAD_PATH.include?(lib_dir)

require 'grpc'
require 'helloworld_services'
require './config'

def main
  credentials = GRPC::Core::ChannelCredentials.new(
    File.read(Config.ca_pem),
    File.read(Config.client_key),
    File.read(Config.client_pem)
  )

  stub = Helloworld::Greeter::Stub.new('rrserver.com:50051', credentials)
  user = ARGV.size > 0 ?  ARGV[0] : 'world'
  message = stub.say_hello(Helloworld::HelloRequest.new(name: user)).message
  p "Greeting: #{message}"
end

main
