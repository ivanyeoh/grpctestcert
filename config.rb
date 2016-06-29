module Config
  KEYDIR = "key_demo"

  def self.client_key
    "#{KEYDIR}/client.key"
  end

  def self.client_pem
    "#{KEYDIR}/client.crt"
  end

  def self.server_key
    "#{KEYDIR}/server.key"
  end

  def self.server_pem
    "#{KEYDIR}/server.crt"
  end
end
