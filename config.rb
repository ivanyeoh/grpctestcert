module Config
  KEYDIR = "key_lala"

  def self.ca_pem
    "#{KEYDIR}/ca.crt"
  end

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
