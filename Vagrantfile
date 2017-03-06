# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant::Config.run do |config|
    config.vm.box = "ubuntu/trusty32"
    config.vm.box_url = "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-i386-vagrant-disk1.box"
    config.vm.forward_port 9000, 9000
    config.vm.share_folder "project", "/home/vagrant/testapp", "."
    config.vm.provision :shell, :path => "etc/install/install.sh", :args => "testapp"
end

